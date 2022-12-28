# -*- coding: utf-8 -*-
import pymince.dictionary


def test_empty():
    assert pymince.dictionary.find_leaf_value("a", {}) == "a"


def test_first_value():
    assert pymince.dictionary.find_leaf_value("a", {"a": "b"}) == "b"


def test_second_value():
    assert pymince.dictionary.find_leaf_value("a", {"a": "b", "b": "c"}) == "c"


def test_third_value():
    assert pymince.dictionary.find_leaf_value("a", {"a": "b", "b": "c", "c": "d"}) == "d"


def test_not_found():
    assert pymince.dictionary.find_leaf_value("a", {"b": "c"}) == "a"


def test_first_not_found():
    assert pymince.dictionary.find_leaf_value("a", {"a": "c", "x": "z"}) == "c"


def test_second_not_found():
    assert pymince.dictionary.find_leaf_value("a", {"a": "b", "b": "c", "d": "e"}) == "c"


def test_first_is_same():
    assert pymince.dictionary.find_leaf_value("a", {"a": "a"}) == "a"


def test_second_is_same():
    assert pymince.dictionary.find_leaf_value("a", {"a": "b", "b": "a"}) == "a"


def test_first_from_none():
    assert pymince.dictionary.find_leaf_value(None, {None: 'a'}) == 'a'
