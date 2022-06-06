"""
Functions that use iterators for efficient loops
"""
import collections
import itertools


def replace(iterable, matcher, new_value, count=-1):
    """
    Returns a generator with all matches of the old "iterable"
    replaced by "new_value".

    :param iterable:
    :param matcher:
    :param new_value:
    :param count:
        Maximum number of occurrences to replace.
        -1 (the default value) means replace all occurrences.
    :return: Replacement generator
    """

    changed = 0
    for obj in iterable:
        if matcher(obj) and (count == -1 or changed < count):
            changed += 1
            yield new_value
        else:
            yield obj


def uniques(iterable, key=None):
    getter = key or (lambda x: x)
    bag = set()
    values = (getter(obj) for obj in iterable) if getter else iter(iterable)
    result = (val for val in values if val in bag or bag.add(val))
    return next(result, None) is None


def uniquer(iterable, key=None):
    getter = key or (lambda x: x)
    bag = set()
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


def all_equal(iterable, key=None):
    grouped = itertools.groupby(iterable, key=key)
    return next(grouped, True) and not next(grouped, False)


def all_distinct(iterable, key=None):
    grouped = itertools.groupby(iterable, key=key)
    return all(is_only_one(group) for _, group in grouped)


def as_not_empty(iterator):
    empty = object()
    first = next(iterator, empty)
    return itertools.chain((first,), iterator) if first is not empty else None


def is_only_one(iterable):
    flag = object()
    return next(iterable, flag) is not flag and next(iterable, flag) is flag


def split(iterable, sep, key=None, maxsplit=-1):
    """
    Split iterable into groups of iterators according
    to given delimiter.

    :param iterable:
    :param sep: The delimiter to split the iterable.
    :param key
        A function to compare the equality of each element with the given delimiter.
        If the key function is not specified or is None, the element itself is used for compare.

    :param maxsplit:
        Maximum number of splits to do.
        -1 (the default value) means no limit.

    :return: Generator with consecutive groups from "iterable" without the delimiter element.
    """

    def group(objects):
        for obj in objects:
            if getter(obj) == sep:
                break
            else:
                yield obj

    def recursive(objects, counter):
        if (iterator := as_not_empty(objects)) and (maxsplit == -1 or counter < maxsplit):
            counter += 1
            yield group(iterator)
            yield from recursive(iterator, counter)
        elif iterator:
            yield iterator
        else:
            return

    getter = key or (lambda x: x)
    return recursive(iter(iterable), 0) if maxsplit else iterable
