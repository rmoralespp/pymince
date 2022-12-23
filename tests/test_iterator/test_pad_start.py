# -*- coding: utf-8 -*-
import pymince.iterator


def test_pad_start_lower_than():
    expected = (None, None, "a", "b", "c")
    result = pymince.iterator.pad_start(("a", "b", "c"), 5)
    assert tuple(result) == expected


def test_pad_start_equal():
    expected = ("a", "b", "c")
    result = pymince.iterator.pad_start(expected, 3)
    assert tuple(result) == expected


def test_pad_start_great_than():
    expected = ("a", "b", "c", "d")
    result = pymince.iterator.pad_start(expected, 3)
    assert tuple(result) == expected


def test_pad_start_empty():
    expected = (None, None, None)
    result = pymince.iterator.pad_start((), 3)
    assert tuple(result) == expected


def test_pad_start_empty_with_fill_value():
    result = pymince.iterator.pad_start((), 2, fill_value="1")
    assert tuple(result) == ("1", "1")
