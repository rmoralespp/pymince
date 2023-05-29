# -*- coding: utf-8 -*-

"""
Useful functions for working with JSON lines data as described:
- http://ndjson.org/
- https://jsonlines.org/
"""

import functools
import json

import pymince._constants
import pymince.file

empty = pymince._constants.empty
dumps_line = functools.partial(json.dumps, ensure_ascii=False)
utf_8 = pymince._constants.utf_8
new_line = "\n"
ext = "jsonl"


def dumper(iterable, **kwargs):
    """Generator yielding JSON lines."""

    encode = functools.partial(dumps_line, **kwargs)
    for obj in iter(iterable):
        yield encode(obj)
        yield new_line


def dumps(iterable, **kwargs):
    """Serialize iterable to a `jsonlines` formatted string."""

    return "".join(dumper(iterable, **kwargs))


def dump(iterable, fp, **kwargs):
    """
    Serialize iterable as a `jsonlines` formatted stream to file.

    :param iterable: Iterable[Any]
    :param fp: file-like object
    :param kwargs: `json.dumps` kwargs

    Example:

    import pymince.jsonlines as jsonl

    with open('myfile.jsonl', mode='w', encoding ='utf-8') as f:
        jsonl.dump(d, f, ensure_ascii=False, indent=2)

    """

    fp.writelines(dumper(iterable, **kwargs))


def dump_into(filename, iterable, encoding=utf_8, **kwargs):
    with open(filename, mode="w", encoding=encoding) as f:
        dump(iterable, f, **kwargs)


def load(fp, **kwargs):
    """
    Returns iterable from a file formatted as JSON lines.

    :param fp: file-like object
    :param kwargs: `json.loads` kwargs
    :rtype: Iterable[Any]
    """

    decode = functools.partial(json.loads, **kwargs)
    yield from map(decode, fp)


def load_from(filename, encoding=utf_8, **kwargs):
    """
    Returns iterable from a filename formatted as JSON lines.

    :param filename: path
    :param encoding: file encoding. 'utf-8' used by default
    :param kwargs: `json.loads` kwargs
    :rtype: Iterable[Any]
    """

    with open(filename, encoding=encoding) as f:
        yield from load(f, **kwargs)
