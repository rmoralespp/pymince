# -*- coding: utf-8 -*-

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


def test_mapping_order_does_not_affect():
    value = "a1 b1"
    mapping = (
        ("a1", "b1"),
        ("b1", "c1"),
    )
    result = pymince.text.multireplace(value, mapping)
    expected = "b1 c1"
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


def test_replace_with_type_error():
    with pytest.raises(TypeError):
        pymince.text.multireplace("1", {1: "foo"})


def test_scape_special_chars():
    rep = (('"', '\\"'), ('\t', '\\t'))
    text = 'And can we span\nmultiple lines?\t"Yes\twe\tcan!"'
    expected = 'And can we span\nmultiple lines?\\t\\"Yes\\twe\\tcan!\\"'
    result = pymince.text.multireplace(text, rep)
    assert result == expected
