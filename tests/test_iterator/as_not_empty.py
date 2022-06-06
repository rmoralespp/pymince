import pymince.iterator


def test_as_not_empty_true():
    expected = (1,)
    result = pymince.iterator.as_not_empty(iter(expected))
    assert tuple(result) == expected


def test_as_not_empty_false():
    result = pymince.iterator.as_not_empty(iter(()))
    assert result is None
