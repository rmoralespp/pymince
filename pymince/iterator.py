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


def not_empty(iterator):
    empty = object()
    first = next(iterator, empty)
    if first is not empty:
        return True, itertools.chain((first,), iterator)
    else:
        return False, iterator
