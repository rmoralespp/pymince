# -*- coding: utf-8 -*-
import pytest

import pymince.iterator


def test_grouper_negative():
    with pytest.raises(ValueError):
        groups = pymince.iterator.grouper(iter((1, 2, 3)), -1)
        tuple(tuple(page) for page in groups)


def test_grouper_zero():
    data = (1, 2, 3)
    groups = pymince.iterator.grouper(iter(data), 0)
    result = tuple(tuple(page) for page in groups)
    assert result == ()


def test_grouper_one():
    data = (1, 2, 3)
    expected = ((1,), (2,), (3,))
    groups = pymince.iterator.grouper(iter(data), 1)
    result = tuple(tuple(page) for page in groups)
    assert result == expected


def test_grouper_many():
    data = (1, 2, 3)
    expected = ((1, 2), (3,))
    groups = pymince.iterator.grouper(iter(data), 2)
    result = tuple(tuple(page) for page in groups)
    assert result == expected
