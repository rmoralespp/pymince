# -*- coding: utf-8 -*-

"""
Useful functions for working with JSON lines data as described:
- http://ndjson.org/
- https://jsonlines.org/
"""

import functools
import json

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
