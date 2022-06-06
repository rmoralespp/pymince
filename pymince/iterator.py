"""
Functions that use iterators for efficient loops
"""
import collections
import itertools


def uniques(iterable, getter=None):
    bag = set()
    values = (getter(obj) for obj in iterable) if getter else iter(iterable)
    result = (val for val in values if val in bag or bag.add(val))
    return next(result, None) is None


def uniquer(iterable, getter=None):
    bag = set()
    getter = getter or (lambda n: n)
    return (bag.add(check) or val for val in iter(iterable) if (check := getter(val)) not in bag)


def grouper(iterable, size):
    slicer = itertools.islice
    values = iter(iterable)
    while True:
        sliced = slicer(values, size)
        try:
            obj = next(sliced)
        except StopIteration:
            break
        else:
            yield itertools.chain((obj,), sliced)


def consume(iterator):
    collections.deque(iterator, maxlen=0)


def all_equal(iterable, getter=None):
    grouped = itertools.groupby(iterable, key=getter)
    return next(grouped, True) and not next(grouped, False)


def all_distinct(iterable, getter=None):
    grouped = itertools.groupby(iterable, key=getter)
    return all(is_only_one(group) for _, group in grouped)


def as_not_empty(iterator):
    empty = object()
    first = next(iterator, empty)
    return itertools.chain((first,), iterator) if first else None


def is_only_one(iterable):
    flag = object()
    return next(iterable, flag) is not flag and next(iterable, flag) is flag


def split(iterable, sep):
    """
    Split iterable into groups of iterators according
    to given delimiter.

    :param iterable:
    :param sep: The delimiter to split the iterable.
    :return: Generator with consecutive groups from "iterable" without the delimiter element.
    """

    def group(objects):
        for obj in objects:
            if obj == sep:
                break
            else:
                yield obj

    iterator = iter(iterable)
    try:
        one = next(iterator)
    except StopIteration:
        return
    else:
        iterator = itertools.chain((one,), iterator)
        yield group(iterator)
        yield from split(iterator, sep)
