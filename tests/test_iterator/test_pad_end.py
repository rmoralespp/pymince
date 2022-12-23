# -*- coding: utf-8 -*-
import pymince.iterator


def test_pad_end_lower_than():
    expected = ("a", "b", "c", None, None)
    result = pymince.iterator.pad_end(("a", "b", "c"), 5)
    assert tuple(result) == expected


def test_pad_end_equal():
    expected = ("a", "b", "c")
    result = pymince.iterator.pad_end(expected, 3)
    assert tuple(result) == expected


def test_pad_end_great_than():
    expected = ("a", "b", "c", "d")
    result = pymince.iterator.pad_end(expected, 3)
    assert tuple(result) == expected


def test_pad_end_empty():
    expected = (None, None, None)
    result = pymince.iterator.pad_end((), 3)
    assert tuple(result) == expected


def test_pad_end_empty_with_fill_value():
    result = pymince.iterator.pad_end((), 2, fill_value="1")
    assert tuple(result) == ("1", "1")
