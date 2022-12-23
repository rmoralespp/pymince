# -*- coding: utf-8 -*-
import pymince.iterator


def test_bool_true_if_not_exhausted():
    it = pymince.iterator.ibool((object(), object()))
    next(it)
    assert it


def test_bool_false_if_exhausted():
    it = pymince.iterator.ibool((object(),))
    next(it)
    assert not it


def test_bool_true():
    assert pymince.iterator.ibool("a")


def test_bool_false():
    assert not pymince.iterator.ibool("")


def test_iter_itself():
    it = pymince.iterator.ibool((1, 2, 3))
    assert it is iter(it)


def test_item_equals():
    expected = items = ("foo", "bar")
    it = pymince.iterator.ibool(items)
    assert tuple(it) == expected


def test_not_consume_if_bool():
    expected = items = ("foo",)
    it = pymince.iterator.ibool(items)
    assert bool(it) is True
    assert tuple(it) == expected
