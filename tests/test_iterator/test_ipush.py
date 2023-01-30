# -*- coding: utf-8 -*-
import pymince.iterator


def test_prepend():
    it = pymince.iterator.ipush(range(1, 3))
    it.prepend(0)
    assert tuple(it) == (0, 1, 2)


def test_multi_prepend():
    it = pymince.iterator.ipush(range(3))
    it.prepend(-1)
    it.prepend(-2)
    assert tuple(it) == (-2, -1, 0, 1, 2)


def test_append():
    it = pymince.iterator.ipush(range(1, 3))
    it.append(0)
    assert tuple(it) == (1, 2, 0)


def test_multi_append():
    it = pymince.iterator.ipush(range(3))
    it.append(-1)
    it.append(-2)
    assert tuple(it) == (0, 1, 2, -1, -2)


def test_append_and_prepend_together():
    it = pymince.iterator.ipush(range(3))
    it.prepend(-1)
    it.prepend(-2)
    it.append(3)
    it.append(4)
    assert tuple(it) == (-2, -1, 0, 1, 2, 3, 4)


def test_iter_itself():
    it = pymince.iterator.ibool((1, 2, 3))
    assert it is iter(it)
