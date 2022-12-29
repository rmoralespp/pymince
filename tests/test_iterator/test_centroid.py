# -*- coding: utf-8 -*-
import pytest

import pymince.iterator


def test_2x2():
    expected = (3, 3)
    coord = iter(((2, 2), (4, 4)))
    res = pymince.iterator.centroid(coord)
    assert tuple(res) == expected


def test_3x2():
    coord = iter(((1, 2), (2, 3), (4, 5)))
    expected = (2.3333333333333335, 3.3333333333333335)
    res = pymince.iterator.centroid(coord)
    assert tuple(res) == expected


def test_3x3_nested_iter():
    p1 = iter((2.100, 2, 1))
    p2 = iter((4.123, 4, 3))
    p3 = iter((4, 4, 9.123))
    expected = (3.4076666666666666, 3.3333333333333335, 4.374333333333333)
    res = pymince.iterator.centroid(iter((p1, p2, p3)))
    assert tuple(res) == expected


def test_0x0():
    res = pymince.iterator.centroid(())
    assert tuple(res) == ()


def test_1x1():
    res = pymince.iterator.centroid(((1,),))
    assert tuple(res) == (1,)


def test_1x2():
    res = pymince.iterator.centroid(((1, 2),))
    assert tuple(res) == (1, 2)


def test_bad():
    coord = iter(((1, 2), (2,), (4, 5, 3)))
    with pytest.raises(TypeError):
        tuple(pymince.iterator.centroid(coord))
