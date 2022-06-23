"""
Functions that use iterators for efficient loops
"""
import collections
import itertools


def replacer(iterable, matcher, new_value, count=-1):
    """
    Make an iterator that returns all occurrences of the old "iterable"
    replaced by "new_value".

    :param iterable:
    :param matcher: Callable to find occurrences. It is an occurrence if the matcher returns True.
    :param new_value: Any value to replace found occurrences.
    :param int count:
        Maximum number of occurrences to replace.
        -1 (the default value) means replace all occurrences.

    Examples:
        from pymince.iterator import replacer

        replacer([1,2,3,1,2,3], lambda n: n == 1, None) # --> None 2 3 None 2 3
        replacer([1,2,3,1,2,3], lambda n: n == 1, None, count=1) # --> None 2 3 1 2 3
    """
    changed = 0
    for obj in iterable:
        if matcher(obj) and (count == -1 or changed < count):
            changed += 1
            yield new_value
        else:
            yield obj


def uniques(iterable, key=None):
    """
    Check if all the elements of a key-based iterable are unique.

    :param iterable:
    :param key: None or "Callable" to compare if iterable items.
    :rtype: bool

    Examples:
        from pymince.iterator import uniques

        uniques([1,2]) # --> True
        uniques([1,1]) # --> False
    """
    getter = key or (lambda x: x)
    bag = set()
    values = (getter(obj) for obj in iterable) if getter else iter(iterable)
    result = (val for val in values if val in bag or bag.add(val))
    return next(result, None) is None


def uniquer(iterable, key=None):
    """
    Make an iterator that returns each element from iterable only once
    respecting the input order.

    Examples:
        from pymince.iterator import uniquer

        uniquer([1, 2, 3, 2]) # --> 1 2 3
    """
    getter = key or (lambda x: x)
    bag = set()
    return (bag.add(check) or val for val in iter(iterable) if (check := getter(val)) not in bag)


def grouper(iterable, size):
    """
    Make an iterator that returns each element being iterable
    with "size" as the maximum number of elements.

    :param iterable:
    :param int size: maximum size of element groups.

    Examples:
        from pymince.iterator import grouper

        groups = grouper([1, 2, 3, 4, 5], 2)
        list(list(g) for g in groups) # --> [[1, 2], [3, 4], [5]]
    """
    slicer = itertools.islice
    values = iter(iterable)
    while True:
        sliced = slicer(values, size)
        if non_empty_sliced := non_empty_or_none(sliced):
            yield non_empty_sliced
        else:
            break


def consume(iterator):
    """
    Completely consume the given iterator.

    Examples:
        from pymince.iterator import consume
        it = iter([1, 2])
        consume(it)
        next(it) # --> StopIteration
    """
    collections.deque(iterator, maxlen=0)


def all_equal(iterable, key=None):
    """
    Check if all the elements of a key-based iterable are equals.

    :param iterable:
    :param key: None or "Callable" to compare if iterable items.
    :rtype: bool

    Examples:
        from pymince.iterator import all_equal

        all_equal([1, 1]) # --> True
        all_equal([1, 2]) # --> False
    """
    grouped = itertools.groupby(iterable, key=key)
    return next(grouped, True) and not next(grouped, False)


def all_distinct(iterable, key=None):
    """
    Check if all the elements of a key-based iterable are distinct.

    :param iterable:
    :param key: None or "Callable" to compare if iterable items.
    :rtype: bool

    Examples:
        from pymince.iterator import all_distinct

        all_distinct([1, 1]) # --> False
        all_distinct([1, 2]) # --> True
    """
    grouped = itertools.groupby(iterable, key=key)
    return all(has_only_one(group) for _, group in grouped)


def non_empty_or_none(iterator):
    """
    Returns an non-empty iterator or None according to given "iterator".

    :param iterator:
    :return: Iterator or None

    Examples:
        from pymince.iterator import non_empty_or_none

        non_empty_or_none([]) # --> None
        non_empty_or_none([1,2]) # --> 1 2
    """

    empty = object()
    first = next(iterator, empty)
    return itertools.chain((first,), iterator) if first is not empty else None


def has_only_one(iterable):
    """
    Check if given iterable has only one element.

    :param iterable:
    :rtype: bool

    Examples:
        from pymince.iterator import has_only_one

        has_only_one([1]) # --> True
        has_only_one([1, 2]) # --> False
        has_only_one([]) # --> False
    """
    flag = object()
    return next(iterable, flag) is not flag and next(iterable, flag) is flag


def splitter(iterable, sep, key=None, maxsplit=-1):
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

    Examples:
        from pymince.iterator import splitter

        data = ["a", "b", "c", "d", "b", "e"]

        undefined_split = splitter(data, "b")
        one_split = splitter(data, "b", maxsplit=1)
        list(list(s) for s in undefined_split) # --> [["a"], ["c", "d"], ["e"]]
        list(list(s) for s in one_split) # --> [["a"], ["c", "d", "b", "e"]]
    """

    def group(objects):
        for obj in objects:
            if getter(obj) == sep:
                break
            else:
                yield obj

    def recursive(objects, counter):
        if (iterator := non_empty_or_none(objects)) and (maxsplit == -1 or counter < maxsplit):
            counter += 1
            yield group(iterator)
            yield from recursive(iterator, counter)
        elif iterator:
            yield iterator
        else:
            return

    getter = key or (lambda x: x)
    return recursive(iter(iterable), 0) if maxsplit else iterable


def pad_start(iterable, length, fill_value=None):
    """
    The function adds "fill_value" at the beginning of the iterable,
    until it reaches the specified length.
    If the value of the "length" param is less than the length of
    the given "iterable", no filling is done.

    :param iterable:
    :param int length: A number specifying the desired length of the resulting iterable.
    :param any fill_value: Any value to fill the given iterable.
    :rtype: Generator

     Examples:
        from pymince.iterator import pad_start

        pad_start(("a", "b"), 3, fill_value="1") # --> "1" "a" "b"
        pad_start(("a", "b"), 3) # --> None "a" "b"
        pad_start(("a", "b", "c"), 3) # --> "a" "b" "c"
    """
    pool = tuple(iter(iterable))
    diff = length - len(pool)
    if diff:
        yield from itertools.repeat(fill_value, diff)
    yield from pool


def pad_end(iterable, length, fill_value=None):
    """
    The function adds "fill_value" at the finishing of the iterable,
    until it reaches the specified length.
    If the value of the "length" param is less than the length of
    the given "iterable", no filling is done.

    :param iterable:
    :param int length: A number specifying the desired length of the resulting iterable.
    :param any fill_value: Any value to fill the given iterable.
    :rtype: Generator

     Examples:
        from pymince.iterator import pad_end

        pad_end(("a", "b"), 3, fill_value="1") # --> "a" "b" "1"
        pad_end(("a", "b"), 3) # --> "a" "b" None
        pad_end(("a", "b", "c"), 3) # --> "a" "b" "c"
    """

    fill = length
    for obj in iter(iterable):
        fill -= 1
        yield obj
    if fill > 0:
        yield from itertools.repeat(fill_value, fill)
