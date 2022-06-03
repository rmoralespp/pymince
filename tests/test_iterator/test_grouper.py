import pymince.iterator


def test_grouper_one():
    data = (1, 2, 3)
    expected = ((1,), (2,), (3,))
    groups = pymince.iterator.grouper(iter(data), 1)
    result = tuple(tuple(page) for page in groups)
    assert result == expected


def test_grouper_many():
    data = (1, 2, 3)
    expected = ((1, 2), (3,))
    groups = pymince.iterator.grouper(iter(data), 2)
    result = tuple(tuple(page) for page in groups)
    assert result == expected
