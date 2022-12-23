# -*- coding: utf-8 -*-
import pymince.iterator


def test_true():
    values = (["b", "a"], iter(("a", "c")), "gta")
    assert pymince.iterator.in_all("a", values)


def test_true_if_empty():
    assert pymince.iterator.in_all("a", ())


def test_false():
    values = iter((["b", "a"], ("c", "a", "d"), "fgh", iter((1, 2))))
    assert not pymince.iterator.in_all("a", values)
