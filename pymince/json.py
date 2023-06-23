# -*- coding: utf-8 -*-
"""Useful functions for working with JSONs."""

import csv
import dataclasses
import datetime
import decimal
import functools
import itertools
import json
import operator
import os
import textwrap
import uuid
import zipfile

dumps = functools.partial(json.dumps, ensure_ascii=False)
dump = functools.partial(json.dump, ensure_ascii=False)
ENCODING = "utf-8"


def load_from(filename, encoding=ENCODING):
    """
    Load JSON from a file using "utf-8" encoding.

    Examples:
        from pymince.json import load_from

        dictionary = load_from("foo.json")
    """
    with open(filename, encoding=encoding) as file:
        return json.load(file)


def dump_into(filename, payload, encoding=ENCODING, **kwargs):
    """
    Dump JSON to a file using "utf-8" encoding.

    Examples:
        from pymince.json import dump_into

        dump_into("foo.json", {"key": "value"})
    """
    with open(filename, "w", encoding=encoding) as file:
        dump(payload, file, **kwargs)


def dump_into_zip(zip_path, arcname, payload, **kwargs):
    """
    Dump JSON into the zip archive under the name arcname.

    Examples:
        from pymince.json import dump_into_zip

        dump_into_zip("archive.zip", "foo.json", {"key": "value"})
    """
    with zipfile.ZipFile(zip_path, mode="w") as zf:
        json_string = dumps(payload, **kwargs)
        zf.writestr(arcname, json_string)


def load_from_zip(zip_path, arcname):
    """
    Load JSON from a file named "arcname" inside a zip archive.

    Examples:
        from pymince.json import load_from_zip

        dictionary = load_from_zip("archive.zip", "foo.json")
    """
    with zipfile.ZipFile(zip_path, mode="r") as zf, zf.open(arcname) as file:
        return json.load(file)


def dump_from_csv(
    csv_path,
    json_path,
    /,
    *,
    fieldnames=None,
    start=0,
    stop=None,
    strip=True,
    encoding=ENCODING,
    **kwargs,
):
    """
    Dump CSV file to a JSON file using "utf-8" encoding.

    :param str csv_path:
    :param str json_path:
    :param fieldnames: list of keys for the JSON
    :param int start:
        If start is specified, will skip all preceding elements;
        otherwise, start defaults to zero.
    :param int stop:
    :param bool strip:
        Whether or not white space should be removed from the
        beginning and end of field values.
    :param str encoding: utf-8 is used by default.
    """

    def read():
        reader = csv.DictReader(csv_f, fieldnames=fieldnames)
        if strip:
            apply = operator.methodcaller("strip")
            for row in reader:
                yield {k and apply(k): (apply(v) if isinstance(v, str) else v) for k, v in row.items()}
        else:
            yield from reader

    with open(csv_path, encoding=encoding, newline="") as csv_f:
        # The official csv doc recommends opening the file with newline='' on all platforms to disable
        # universal newlines translation.

        data = itertools.islice(read(), start, stop)
        idump_into(json_path, data, encoding=encoding, **kwargs)


def idump_lines(iterable, **dumps_kwargs):
    """
    Generator yielding string lines that form a JSON array
    with the serialized elements of given iterable.
    *** Useful to reduce memory consumption ***

    :param iterable: Iterable[dict]
    :rtype: Iterable[str]
    """

    it = iter(iterable)
    encode = functools.partial(dumps, **dumps_kwargs)
    indent = dumps_kwargs.get("indent")
    prefix = " " * indent if indent else ""
    yield "[\n"
    obj = next(it, None)
    if obj is not None:
        yield textwrap.indent(encode(obj), prefix)
    for obj in it:
        yield ",\n"
        yield textwrap.indent(encode(obj), prefix)
    yield "\n"
    yield "]"


def idump_into(filename, iterable, encoding=ENCODING, **kwargs):
    """
    Dump an iterable incrementally into a JSON file
    using the "utf-8" encoding.
    The result will always be an array with the elements of the iterable.
    *** Useful to reduce memory consumption ***

    Examples:
        from pymince.json import idump_into

        it = iter([{"key": "foo"}, {"key": "bar"}])
        dump_into("foo.json", it)
    """

    with open(filename, mode="w", encoding=encoding) as f:
        f.writelines(idump_lines(iterable, **kwargs))


def idump_fork(path_items, encoding=ENCODING, dump_if_empty=True, **dumps_kwargs):
    """
    Incrementally dumps different groups of elements into
    the indicated JSON file.
    *** Useful to reduce memory consumption ***

    :param Iterable[file_path, Iterable[dict]] path_items: group items by file path
    :param encoding: 'utf-8' by default.
    :param bool dump_if_empty: If false, don't create an empty file.
    :param dumps_kwargs: json.dumps kwargs.

    Examples:
        from pymince.json import idump_fork

        path_items = (
            ("num.json", ({"value": 1}, {"value": 2})),
            ("num.json", ({"value": 3},)),
            ("foo.json", ({"a": "1"}, {"b": 2})),
            ("baz.json", ()),
        )
        idump_fork(iter(path_items))
    """

    def get_dumper(dst):
        nothing = True
        with open(dst, mode="w", encoding=encoding) as fd:
            write = fd.write
            write("[\n")
            try:
                while True:
                    obj = yield
                    if nothing:
                        nothing = False
                    else:
                        write(",\n")
                    write(textwrap.indent(encode(obj), prefix))
            except GeneratorExit:
                write("]") if nothing else write("\n]")

        if nothing and not dump_if_empty:
            os.unlink(dst)

    encode = functools.partial(dumps, **dumps_kwargs)
    indent = dumps_kwargs.get("indent")
    prefix = " " * indent if indent else ""

    dumpers = dict()
    for path, items in path_items:
        if path in dumpers:
            dumper = dumpers[path]
        else:
            dumper = get_dumper(path)
            dumper.send(None)
            dumpers[path] = dumper

        for item in items:
            dumper.send(item)
    # Cleanup
    for dumper in dumpers.values():
        dumper.close()


class JSONEncoder(json.JSONEncoder):
    """
    JSON encoder that handles additional types compared
    to `json.JSONEncoder`

    - `datetime` and `date` are serialized to strings according to the isoformat.
    - `decimal.Decimal` is serialized to a string.
    - `uuid.UUID` is serialized to a string.
    - `dataclasses.dataclass` is passed to `dataclasses.asdict`.
    - `frozenset` and `set` are serialized by ordering their values.
    """

    def default(self, obj):
        if isinstance(obj, datetime.date):
            return obj.isoformat()
        elif isinstance(obj, (frozenset, set)):
            return sorted(obj)
        elif isinstance(obj, (decimal.Decimal, uuid.UUID)):
            return str(obj)
        elif dataclasses.is_dataclass(obj):
            return dataclasses.asdict(obj)
        else:
            # Let the base class default method raise the TypeError
            return super().default(obj)
