import operator

import pymince.iterator


def test_all_distinct_false():
    assert not pymince.iterator.all_distinct((1, 1))


def test_all_distinct_true():
    assert pymince.iterator.all_distinct((1, 2))


def test_all_distinct_false_given_itemgetter():
    getter = operator.itemgetter("name")
    data = (
        {"id": 1, "name": "n1"},
        {"id": 2, "name": "n1"},
    )
    assert not pymince.iterator.all_distinct(data, getter=getter)


def test_all_distinct_true_given_itemgetter():
    getter = operator.itemgetter("name")
    data = (
        {"id": 1, "name": "n1"},
        {"id": 2, "name": "n2"},
    )
    assert pymince.iterator.all_distinct(data, getter=getter)
