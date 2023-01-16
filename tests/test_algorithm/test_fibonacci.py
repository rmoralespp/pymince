# -*- coding: utf-8 -*-

import pymince.algorithm


def test_fibonacci_n_lt_0():
    expected = ()
    res = pymince.algorithm.fibonacci(n=-1)
    assert tuple(res) == expected


def test_fibonacci_n_eq_0():
    expected = ()
    res = pymince.algorithm.fibonacci(n=0)
    assert tuple(res) == expected


def test_fibonacci_n_eq_10():
    expected = (0, 1, 1, 2, 3, 5, 8)
    res = pymince.algorithm.fibonacci(n=10)
    assert tuple(res) == expected


def test_fibonacci_float_n():
    expected = (0, 1, 1, 2, 3, 5, 8)
    res = pymince.algorithm.fibonacci(n=10.4)
    assert tuple(res) == expected
