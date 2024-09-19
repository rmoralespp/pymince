# -*- coding: utf-8 -*-

"""
Useful functions for working with JSONs.
- Supports `orjson`, `ujson` libraries or standard `json`.
- Supports following compression formats: gzip => (.gz), bzip2 => (.bz2), xz => (.xz)
"""

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

import pymince._constants
import pymince.file

# Use the fastest available JSON library for serialization/deserialization, prioritizing `orjson`,
# then `ujson`, and defaulting to the standard `json` if none are installed.
try:
    import orjson
except ImportError:
    orjson = None

try:
    import ujson
except ImportError:
    ujson = None

PROVIDER = orjson or ujson or json
ENCODING = pymince._constants.utf_8

json_dumps = functools.partial(PROVIDER.dumps, ensure_ascii=False)
json_dump = functools.partial(PROVIDER.dump, ensure_ascii=False)
json_load = (orjson or ujson or json).load


def load_from(filename, encoding=ENCODING):
    """
    Load JSON from a file.
    - Recognizes (`.gz`, `.xz`, `.bz2`) extensions to load compressed files.
    - Loads falls back to the functions: (`orjson.load`, `ujson.load`, and `json.load`).

    Examples:
        from pymince.json import load_from

        dictionary1 = load_from("foo.json")     # uncompressed
        dictionary2 = load_from("foo.json.gz")  # gzip-compressed
        dictionary3 = load_from("foo.json.xz")  # lzma-compressed
        dictionary4 = load_from("foo.json.bz2") # bz2-compressed
    """

    with pymince.file.xopen(filename, mode="rt", encoding=encoding) as file:
        return json.load(file)


def dump_into(filename, obj, encoding=ENCODING, **kwargs):
    """
    Dump JSON to a file.
    - Use (`.gz`, `.xz`, `.bz2`) extensions to create compressed files.
    - Dumps falls back to the functions: (`orjson.dump`, `ujson.dump`, and `json.dump`).

    Examples:
        from pymince.json import dump_into

        dump_into("foo.json", {"key": "value"})     # uncompressed
        dump_into("foo.json.gz", {"key": "value"})  # gzip-compressed
        dump_into("foo.json.xz", {"key": "value"})  # lzma-compressed
        dump_into("foo.json.bz2", {"key": "value"}) # bz2-compressed
    """

    with pymince.file.xopen(filename, mode="wt", encoding=encoding) as fd:
        json_dump(obj, fd, **kwargs)


def dump_into_zip(zip_path, arcname, payload, **kwargs):
    """
    Dump JSON into the zip archive under the name arcname.

    Examples:
        from pymince.json import dump_into_zip

        dump_into_zip("archive.zip", "foo.json", {"key": "value"})
    """

    with zipfile.ZipFile(zip_path, mode="w") as zf:
        json_string = json_dumps(payload, **kwargs)
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
    Dump CSV file to a JSON file.
    - Use (`.gz`, `.xz`, `.bz2`) extensions to create a compressed file.
    - Dumps falls back to the functions: (`orjson.dumps`, `ujson.dumps`, and `json.dumps`).

    :param str csv_path:
    :param str json_path:
    :param fieldnames: list of keys for the JSON
    :param int start:
        If start is specified, will skip all preceding elements;
        otherwise, start defaults to zero.
    :param int stop:
    :param bool strip:
        Whether white space should be removed from the
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
    - Dumps falls back to the functions: (`orjson.dumps`, `ujson.dumps`, and `json.dumps`).

    :param iterable: Iterable[dict]
    :rtype: Iterable[str]
    """

    it = iter(iterable)
    encode = functools.partial(json_dumps, **dumps_kwargs)
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
    Dump an iterable incrementally into a JSON file.
    - Use (`.gz`, `.xz`, `.bz2`) extensions to create compressed files.
    - Dumps falls back to the functions: (`orjson.dumps`, `ujson.dumps`, and `json.dumps`).

    The result will always be an array with the elements of the iterable.
    *** Useful to reduce memory consumption ***

    Examples:
        from pymince.json import idump_into

        values = ([{"key": "foo"}, {"key": "bar"}])

        idump_into("foo.json", values)     # uncompressed
        idump_into("foo.json.gz", values)  # gzip-compressed
        idump_into("foo.json.xz", values)  # lzma-compressed
        idump_into("foo.json.bz2", values) # bz2-compressed
    """

    with pymince.file.xopen(filename, mode="wt", encoding=encoding) as f:
        f.writelines(idump_lines(iterable, **kwargs))


def idump_fork(path_items, encoding=ENCODING, dump_if_empty=True, **dumps_kwargs):
    """
    Incrementally dumps different groups of elements into
    the indicated JSON file.
    *** Useful to reduce memory consumption ***

    - Use (`.gz`, `.xz`, `.bz2`) extensions to create compressed files.
    - Dumps falls back to the functions: (`orjson.dumps`, `ujson.dumps`, and `json.dumps`).

    :param Iterable[file_path, Iterable[dict]] path_items: group items by file path
    :param encoding: 'utf-8' by default.
    :param bool dump_if_empty: If false, don't create an empty file.
    :param dumps_kwargs: json.dumps kwargs.

    Examples:
        from pymince.json import idump_fork

        path_items = (
            ("num.json.gz", ({"value": 1}, {"value": 2})),
            ("num.json.gz", ({"value": 3},)),
            ("foo.json", ({"a": "1"}, {"b": 2})),
            ("baz.json", ()),
        )
        idump_fork(iter(path_items))
    """

    def get_dumper(dst):
        nothing = True
        with pymince.file.xopen(dst, mode="wt", encoding=encoding) as fd:
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

    encode = functools.partial(json_dumps, **dumps_kwargs)
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
