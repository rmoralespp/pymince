# -*- coding: utf-8 -*-
import pytest

import pymince.iterator


def test_empty():
    with pytest.raises(TypeError):
        pymince.iterator.sub(())


def test_single():
    assert pymince.iterator.sub(iter((1,))) == 1


def test_many():
    assert pymince.iterator.sub(iter((0, 1, 2, 3.5))) == -6.5


def test_with_zero():
    assert pymince.iterator.sub(iter((1, 0))) == 1


def test_with_type_error():
    with pytest.raises(TypeError):
        pymince.iterator.sub("abcd")


def test_with_sets():
    assert pymince.iterator.sub(({1, 2, 3, 4}, {4, 5, 6}, {1, 7, 8, 9})) == {2, 3}
