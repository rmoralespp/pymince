import pymince.iterator


def test_only_one_true():
    assert pymince.iterator.is_only_one(iter((1,)))


def test_only_one_false_if_many():
    assert not pymince.iterator.is_only_one(iter((1, 2)))


def test_only_one_false_if_empty():
    assert not pymince.iterator.is_only_one(iter(()))
