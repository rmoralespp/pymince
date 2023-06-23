# -*- coding: utf-8 -*-

"""
Useful functions for working with JSON lines data as described:
- http://ndjson.org/
- https://jsonlines.org/
"""

import functools
import json
import os

import pymince._constants

empty = pymince._constants.empty
dumps_line = functools.partial(json.dumps, ensure_ascii=False)
utf_8 = pymince._constants.utf_8
new_line = "\n"


def dumper(iterable, **kwargs):
    """Generator yielding JSON lines."""

    encode = functools.partial(dumps_line, **kwargs)
    for obj in iter(iterable):
        yield encode(obj)
        yield new_line


def dumps(iterable, **kwargs):
    """
    Serialize iterable to a `jsonlines` formatted string.

    :param iterable: Iterable[Any]
    :param kwargs: `json.dumps` kwargs
    :rtype: str
    """

    return "".join(dumper(iterable, **kwargs))


def dump(iterable, fp, **kwargs):
    """
    Serialize iterable as a `jsonlines` formatted stream to file.

    :param iterable: Iterable[Any]
    :param fp: file-like object
    :param kwargs: `json.dumps` kwargs

    Example:
        from pymince.jsonlines import dump

        data = ({'foo': 1}, {'bar': 2})
        with open('myfile.jsonl', mode='w', encoding ='utf-8') as file:
            dump(iter(data), file)
    """

    fp.writelines(dumper(iterable, **kwargs))


def dump_into(filename, iterable, encoding=utf_8, **kwargs):
    """
    Dump iterable to a `jsonlines` file.

    Example:
        from pymince.jsonlines import dump_into

        data = ({'foo': 1}, {'bar': 2})
        dump_into("myfile.jsonl", iter(data))
    """

    with open(filename, mode="w", encoding=encoding) as f:
        dump(iterable, f, **kwargs)


def dump_fork(path_items, encoding=utf_8, dump_if_empty=True, **kwargs):
    """
    Incrementally dumps different groups of elements into
    the indicated `jsonlines` file.
    *** Useful to reduce memory consumption ***

    :param Iterable[file_path, Iterable[dict]] path_items: group items by file path
    :param encoding: 'utf-8' by default.
    :param bool dump_if_empty: If false, don't create an empty `jsonlines` file.
    :param kwargs: json.dumps kwargs.

    Examples:
        from pymince.jsonlines import dump_fork

        path_items = (
            ("num.jsonl", ({"value": 1}, {"value": 2})),
            ("num.jsonl", ({"value": 3},)),
            ("foo.jsonl", ({"a": "1"}, {"b": 2})),
            ("baz.jsonl", ()),
        )
        dump_fork(iter(path_items))
    """

    def get_writer(dst):
        nothing = True
        with open(dst, mode="w", encoding=encoding) as fd:
            try:
                while True:
                    obj = yield
                    if nothing:
                        nothing = False
                    else:
                        fd.write(new_line)
                    fd.write(encoder(obj))
            except GeneratorExit:
                pass
        if nothing and not dump_if_empty:
            os.unlink(dst)

    encoder = functools.partial(dumps_line, **kwargs)
    writers = dict()

    for path, items in path_items:
        if path in writers:
            writer = writers[path]
        else:
            writer = get_writer(path)
            writer.send(None)
            writers[path] = writer

        for item in items:
            writer.send(item)
    # Cleanup
    for writer in writers.values():
        writer.close()


def load(fp, **kwargs):
    """
    Returns iterable from a file formatted as JSON lines.

    :param fp: file-like object
    :param kwargs: `json.loads` kwargs
    :rtype: Iterable[str]
    """

    decode = functools.partial(json.loads, **kwargs)
    yield from map(decode, fp)


def load_from(filename, encoding=utf_8, **kwargs):
    """
    Returns iterable from a filename formatted as JSON lines.

    :param filename: path
    :param encoding: file encoding. 'utf-8' used by default
    :param kwargs: `json.loads` kwargs
    :rtype: Iterable[str]

    Examples:
        from pymince.jsonlines import load_from

        it = load_from("myfile.jsonl")
        next(it)
    """

    with open(filename, encoding=encoding) as f:
        yield from load(f, **kwargs)
