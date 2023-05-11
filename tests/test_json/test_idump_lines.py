# -*- coding: utf-8 -*-
import json

import pymince.json


def test_dumped_iterable_list_with_one_element():
    data = [
        {"key": "ñó", "nested": [1, 2, 3]},
    ]
    result = pymince.json.idump_lines(iter(data))
    result = json.loads("".join(result))
    assert result == data


def test_dumped_iterable_list_with_two_elements():
    data = [
        {"ab": "foo"},
        {"bc": "foo"},
    ]
    result = pymince.json.idump_lines(iter(data))
    result = json.loads("".join(result))
    assert result == data


def test_dumped_empty():
    result = pymince.json.idump_lines([])
    result = json.loads("".join(result))
    assert result == []


def test_dumped_dict():
    data = {"a": 1, "b": 2, "c": 3}
    result = pymince.json.idump_lines(data)
    result = json.loads("".join(result))
    expected = ["a", "b", "c"]
    assert result == expected


def test_dumped_set():
    data = {"a", "b", "c"}
    result = pymince.json.idump_lines(data)
    result = json.loads("".join(result))
    assert result == list(data)


def test_dumped_str():
    data = "abc"
    result = pymince.json.idump_lines(data)
    result = json.loads("".join(result))
    assert result == list(data)
