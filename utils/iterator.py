import collections
import itertools


def uniques(iterable, getter):
    bag = set()
    values = (getter(obj) for obj in iterable)
    result = (val for val in values if val in bag or bag.add(val))
    return next(result, None) is None


def uniquer(iterable, getter=None):
    getter = getter or (lambda n: n)
    bag = set()
    return (bag.add(check) or val for val in iterable if (check := getter(val)) not in bag)


def grouper(iterable, size):
    slicer = itertools.islice
    iterator = iter(iterable)
    while True:
        sliced = slicer(iterator, size)
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
