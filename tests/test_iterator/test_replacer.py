import pymince.iterator


def test_replace_one():
    values = (1, 1, 1)
    matcher = lambda n: n == 1
    result = pymince.iterator.replacer(values, matcher, "foo", count=1)
    assert tuple(result) == ("foo", 1, 1)


def test_replace_two():
    values = (1, 1, 1)
    matcher = lambda n: n == 1
    result = pymince.iterator.replacer(values, matcher, "foo", count=2)
    assert tuple(result) == ("foo", "foo", 1)


def test_replace_undefined():
    values = (1,) * 100
    matcher = lambda n: n == 1
    result = pymince.iterator.replacer(values, matcher, "foo")
    assert tuple(result) == ("foo",) * 100


def test_replace_heterogeneous():
    values = (1, 2, 3, 1, 2, 3)
    matcher = lambda n: n == 1
    result = pymince.iterator.replacer(values, matcher, "foo")
    assert tuple(result) == ('foo', 2, 3, 'foo', 2, 3)
