# -*- coding: utf-8 -*-
import pymince.iterator


def test_all_identical_true():
    a, b = object(), object()
    assert pymince.iterator.all_identical([a, b, a], [a, b, a])


def test_all_identical_false():
    a, b = object(), object()
    # new list object, while "equal" is not "identical"
    assert not pymince.iterator.all_identical([a, b, [a]], [a, b, [a]])
