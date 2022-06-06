import pytest

import pymince.iterator


def test_split_start_with_sep():
    result = pymince.iterator.split((1, 2, 3), 1)
    assert tuple(tuple(group) for group in result) == ((), (2, 3))


def test_split_end_with_sep():
    result = pymince.iterator.split((1, 2, 3), 3)
    assert tuple(tuple(group) for group in result) == ((1, 2),)


def test_split_contains_sep():
    result = pymince.iterator.split((1, 2, 3), 2)
    assert tuple(tuple(group) for group in result) == ((1,), (3,))


@pytest.mark.parametrize("data,sep,maxsplit,expected", [
    ((1, 2, 3, 1, 2, 3, 1, 2, 1), 1, 0, (1, 2, 3, 1, 2, 3, 1, 2, 1)),
    ((1, 2, 3, 1, 2, 3, 1, 2, 1), 1, 1, ((), (2, 3, 1, 2, 3, 1, 2, 1))),
    ((1, 2, 3, 1, 2, 3, 1, 2, 1), 1, 2, ((), (2, 3), (2, 3, 1, 2, 1))),
    ((1, 2, 3, 1, 2, 3, 1, 2, 1), 1, 3, ((), (2, 3), (2, 3), (2, 1))),
    ((1, 2, 3, 1, 2, 3, 1, 2, 1), 1, 4, ((), (2, 3), (2, 3), (2,))),
    ((1, 2, 3, 1, 2, 3, 1, 2, 1), 1, -1, ((), (2, 3), (2, 3), (2,))),
])
def test_split_multi_sep(data, sep, maxsplit, expected):
    result = pymince.iterator.split(data, sep, maxsplit=maxsplit)
    if maxsplit:
        assert tuple(tuple(group) for group in result) == expected
    else:
        assert tuple(result) == expected


def test_split_no_contains_sep():
    result = pymince.iterator.split((1, 2, 3), 0)
    assert tuple(tuple(group) for group in result) == ((1, 2, 3),)


def test_next_group_on_long_iterable():
    result = pymince.iterator.split(range(1000000), 2)
    assert tuple(next(result)) == (0, 1)


def test_split_empty():
    result = pymince.iterator.split((), 1)
    assert tuple(result) == ()
