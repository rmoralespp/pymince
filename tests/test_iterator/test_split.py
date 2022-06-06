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


def test_split_multi_sep():
    data = (1, 2, 3, 1, 2, 3, 1, 2, 1)
    result = pymince.iterator.split(data, 1)
    assert tuple(tuple(group) for group in result) == ((), (2, 3), (2, 3), (2,))


def test_split_no_contains_sep():
    result = pymince.iterator.split((1, 2, 3), 0)
    assert tuple(tuple(group) for group in result) == ((1, 2, 3),)


def test_next_group_on_long():
    result = pymince.iterator.split(range(1000000), 2)
    assert tuple(next(result)) == (0, 1)
