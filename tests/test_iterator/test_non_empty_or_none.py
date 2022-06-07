import pymince.iterator


def test_non_empty_or_none_if_not_none():
    expected = (1,)
    result = pymince.iterator.non_empty_or_none(iter(expected))
    assert tuple(result) == expected


def test_non_empty_or_none_if_none():
    result = pymince.iterator.non_empty_or_none(iter(()))
    assert result is None
