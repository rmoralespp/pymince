# -*- coding: utf-8 -*-
import pytest

import pymince.iterator


def test_empty():
    with pytest.raises(TypeError):
        pymince.iterator.truediv(())


def test_single():
    assert pymince.iterator.truediv(iter((1,))) == 1


def test_many():
    assert pymince.iterator.truediv(iter((2, 3.6))) == 0.5555555555555556


def test_with_zero_error():
    with pytest.raises(ZeroDivisionError):
        pymince.iterator.truediv(iter((1, 2, 0, 4)))


def test_with_type_error():
    with pytest.raises(TypeError):
        pymince.iterator.truediv("abcd")
