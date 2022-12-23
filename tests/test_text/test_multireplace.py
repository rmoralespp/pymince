# -*- coding: utf-8 -*-
import datetime

import pytest

import pymince.text


def test_replace_one():
    value = "foo1 var1 baz1 bar1 ño1"
    mapping = {
        "var1": "var2",
    }
    result = pymince.text.multireplace(value, mapping)
    expected = "foo1 var2 baz1 bar1 ño1"
    assert result == expected


def test_replace_many_with_dict():
    value = "foo1 var1 baz1 bar1 ño1"
    mapping = {
        "var1": "var2",
        "bar1": "bar1",
        "ño1": "ño2",
    }
    result = pymince.text.multireplace(value, mapping)
    expected = "foo1 var2 baz1 bar1 ño2"
    assert result == expected


def test_replace_many_with_exchange():
    value = "foo1 var1 baz1"
    mapping = {
        "foo1": "baz1",
        "baz1": "foo1",
    }
    result = pymince.text.multireplace(value, mapping)
    expected = "baz1 var1 foo1"
    assert result == expected


def test_replace_many_with_tuple():
    value = "foo1 var1 baz1 bar1 ño1"
    mapping = (
        ("var1", "var2"),
        ("bar1", "bar1"),
        ("ño1", "ño2"),
    )
    result = pymince.text.multireplace(value, mapping)
    expected = "foo1 var2 baz1 bar1 ño2"
    assert result == expected


def test_replacement_no_match():
    expected = value = "foo"
    mapping = {
        "var1": "var2",
    }
    result = pymince.text.multireplace(value, mapping)
    assert result == expected


def test_replace_with_empty_text_arg():
    expected = value = ""
    mapping = {
        "var1": "var2",
    }
    result = pymince.text.multireplace(value, mapping)
    assert result == expected


def test_replace_with_empty_replacements_arg():
    expected = value = "foo"
    result = pymince.text.multireplace(value, {})
    assert result == expected


def test_replace_with_other_types():
    value = "to_int to_float to_tuple to_list to_dict to_date to_regexp"

    mapping = {
        "to_int": 1,
        "to_float": 1.20,
        "to_tuple": (1, 2, 3, 4),
        "to_list": [1, 2, 3, 4],
        "to_dict": {"a": [5], "b": "foo", "c": "Ñí"},
        "to_date": datetime.datetime(2022, 12, 12),
        "to_regexp": r"<\w+>",
    }

    expected = "1 1.2 (1, 2, 3, 4) [1, 2, 3, 4] {'a': [5], 'b': 'foo', 'c': 'Ñí'} 2022-12-12 00:00:00 <\\w+>"
    result = pymince.text.multireplace(value, mapping)
    assert result == expected


def test_replace_with_type_error():
    with pytest.raises(TypeError):
        pymince.text.multireplace("1", {1: "foo"})
