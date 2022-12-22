import operator

import pytest

import pymince.iterator


def test_splitter_on_string():
    result = pymince.iterator.splitter("eat sleep repeat", " ")
    assert ",".join("".join(group) for group in result) == "eat,sleep,repeat"


def test_splitter_start_with_sep():
    data = (1, 2, 3)
    expected = ((), (2, 3))
    result = pymince.iterator.splitter(data, 1)
    assert tuple(tuple(group) for group in result) == expected


def test_splitter_end_with_sep():
    data = (1, 2, 3)
    expected = ((1, 2),)
    result = pymince.iterator.splitter(data, 3)
    assert tuple(tuple(group) for group in result) == expected


def test_splitter_contains_sep():
    data = (1, 2, 3)
    expected = ((1,), (3,))
    result = pymince.iterator.splitter(data, 2)
    assert tuple(tuple(group) for group in result) == expected


def test_splitter_start_with_sep_given_itemgetter():
    sep = 1
    key = operator.itemgetter(0)
    val = ((1, "foo"), (2, "foo"), (3, "foo"))
    exc = ((), ((2, "foo"), (3, "foo")))
    res = pymince.iterator.splitter(val, sep, key=key)
    assert tuple(tuple(group) for group in res) == exc


def test_splitter_end_with_sep_given_itemgetter():
    sep = 3
    key = operator.itemgetter(0)
    val = ((1, "abc"), (2, "bcd"), (3, "def"))
    exc = (((1, "abc"), (2, "bcd")),)
    res = pymince.iterator.splitter(val, sep, key=key)
    assert tuple(tuple(group) for group in res) == exc


def test_splitter_contains_sep_given_itemgetter():
    sep = 2
    key = operator.itemgetter(0)
    val = ((1, "abc"), (2, "bcd"), (3, "def"))
    exc = (((1, "abc"),), ((3, "def"),))
    res = pymince.iterator.splitter(val, sep, key=key)
    assert tuple(tuple(group) for group in res) == exc


@pytest.mark.parametrize(
    "maxsplit,expected",
    [
        (0, (1, 2, 3, 1, 2, 3, 1, 2, 1)),
        (1, ((), (2, 3, 1, 2, 3, 1, 2, 1))),
        (2, ((), (2, 3), (2, 3, 1, 2, 1))),
        (3, ((), (2, 3), (2, 3), (2, 1))),
        (4, ((), (2, 3), (2, 3), (2,))),
        (-1, ((), (2, 3), (2, 3), (2,))),
    ],
)
def test_splitter_multi_sep(maxsplit, expected):
    data = (1, 2, 3, 1, 2, 3, 1, 2, 1)
    sep = 1
    result = pymince.iterator.splitter(data, sep, maxsplit=maxsplit)
    if maxsplit:
        assert tuple(tuple(group) for group in result) == expected
    else:
        assert tuple(result) == expected


def test_splitter_no_contains_sep():
    data = (1, 2, 3)
    expected = ((1, 2, 3),)
    result = pymince.iterator.splitter(data, 0)
    assert tuple(tuple(group) for group in result) == expected


def test_splitter_no_contains_sep_give_itemgetter():
    data = ((1, "foo"), (2, "foo"), (3, "foo"))
    expected = (data,)
    result = pymince.iterator.splitter(data, 0)
    assert tuple(tuple(group) for group in result) == expected


def test_next_group_on_long_iterable():
    result = pymince.iterator.splitter(range(1000000), 2)
    assert tuple(next(result)) == (0, 1)


def test_splitter_empty():
    result = pymince.iterator.splitter((), 1)
    assert tuple(result) == ()
