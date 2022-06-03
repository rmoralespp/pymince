import pymince.iterator


def test_not_empty_true():
    expected = (1,)
    is_not_empty, result = pymince.iterator.not_empty(iter(expected))
    assert is_not_empty
    assert tuple(result) == expected


def test_not_empty_false():
    expected = ()
    is_not_empty, result = pymince.iterator.not_empty(iter(expected))
    assert not is_not_empty
    assert tuple(result) == expected
