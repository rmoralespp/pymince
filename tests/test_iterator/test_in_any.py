# -*- coding: utf-8 -*-
import pymince.iterator


def test_false():
    values = (["b"], ("c", "d"), "fgh", iter((1, 2)))
    assert not pymince.iterator.in_any("a", values)


def test_false_if_empty():
    assert not pymince.iterator.in_any("a", ())


def test_true_endswith():
    values = (("b", "c", "d"), "fgh", iter((1, 2)), ["a"])
    assert pymince.iterator.in_any("a", values)


def test_true_startswith():
    values = (("a", "c", "d"), "fgh", iter((1, 2)), ["z"])
    assert pymince.iterator.in_any("a", values)
