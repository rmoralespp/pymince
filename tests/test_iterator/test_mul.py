# -*- coding: utf-8 -*-
import pytest

import pymince.iterator


def test_empty():
    assert pymince.iterator.mul(()) == 1


def test_single():
    assert pymince.iterator.mul(iter((1,))) == 1


def test_single_with_start():
    assert pymince.iterator.mul(iter((1,)), start=2) == 2


def test_many():
    assert pymince.iterator.mul(iter((2, 3, 5.5))) == 33.0


def test_many_with_start():
    assert pymince.iterator.mul(iter((2, 3)), start=2) == 12


def test_with_zero():
    assert pymince.iterator.mul(iter((1, 2, 0, 4))) == 0


def test_with_type_error():
    with pytest.raises(TypeError):
        pymince.iterator.sub("abcd")
