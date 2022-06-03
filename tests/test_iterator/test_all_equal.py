import operator

import pymince.iterator


def test_all_equal_true():
    assert pymince.iterator.all_equal((1, 1))


def test_all_equal_false():
    assert not pymince.iterator.all_equal((1, 2))


def test_all_equal_true_given_itemgetter():
    getter = operator.itemgetter("name")
    data = (
        {"id": 1, "name": "n1"},
        {"id": 2, "name": "n1"},
    )
    assert pymince.iterator.all_equal(data, getter=getter)


def test_all_equal_false_given_itemgetter():
    getter = operator.itemgetter("name")
    data = (
        {"id": 1, "name": "n1"},
        {"id": 2, "name": "n2"},
    )
    assert not pymince.iterator.all_equal(data, getter=getter)
