# -*- coding: utf-8 -*-
import pytest

import pymince.algorithm


def test_fibonacci_n_lt_0():
    with pytest.raises(ValueError):
        pymince.algorithm.fibonacci(n=-1)


def test_fibonacci_n_eq_0():
    expected = ()
    res = pymince.algorithm.fibonacci(n=0)
    assert tuple(res) == expected


def test_fibonacci_n_eq_10():
    expected = (0, 1, 1, 2, 3, 5, 8, 13, 21, 34)
    res = pymince.algorithm.fibonacci(n=10)
    assert tuple(res) == expected
