import operator

import pymince.iterator


def test_all_equals_true():
    a = b = range(10)
    assert pymince.iterator.all_equals(a, b)


def test_all_equals_true_with_diff_types():
    def gen_f():
        yield from (1, 2, 3)

    a = range(1, 4)
    b = (1, 2, 3)
    c = iter((1, 2, 3))
    d = {1, 2, 3}
    e = dict.fromkeys((1, 2, 3), None)
    f = gen_f()
    assert pymince.iterator.all_equals(a, b, c, d, e, f)


def test_all_equals_true_if_empty():
    assert pymince.iterator.all_equals()


def test_all_equals_false():
    a = range(1, 10, 2)
    b = range(1, 10, 3)
    assert not pymince.iterator.all_equals(a, b)


def test_all_equals_true_given_itemgetter():
    getter = operator.itemgetter("name")
    a = (
        {"id": 1, "name": "n1"},
        {"id": 2, "name": "n2"},
    )
    b = (
        {"id": 3, "name": "n1"},
        {"id": 4, "name": "n2"},
    )
    assert pymince.iterator.all_equals(a, b, key=getter)


def test_all_equals_false_given_itemgetter():
    getter = operator.itemgetter("name")
    a = (
        {"id": 1, "name": "n1"},
        {"id": 2, "name": "n2"},
    )
    b = (
        {"id": 3, "name": "n3"},
        {"id": 4, "name": "n4"},
    )
    assert not pymince.iterator.all_equals(a, b, key=getter)
