# -*- coding: utf-8 -*-
import os
import tempfile

import pymince.json


def test_dumped_iterable_list_with_one_element():
    data = [
        {"key": "ñó", "nested": [1, 2, 3]},
    ]
    it = iter(data)
    with tempfile.TemporaryDirectory() as tmpdir:
        filename = os.path.join(tmpdir, "foo.json")
        pymince.json.idump_into(filename, it)
        dumped = pymince.json.load_from(filename)

    assert dumped == data


def test_dumped_iterable_list_with_two_elements():
    data = [
        {"ab": "foo"},
        {"bc": "foo"},
    ]
    it = iter(data)
    with tempfile.TemporaryDirectory() as tmpdir:
        filename = os.path.join(tmpdir, "foo.json")
        pymince.json.idump_into(filename, it)
        dumped = pymince.json.load_from(filename)

    assert dumped == data


def test_dumped_iterable_dict():
    data = {"a": 1, "b": 2}
    it = iter(data)
    with tempfile.TemporaryDirectory() as tmpdir:
        filename = os.path.join(tmpdir, "foo.json")
        pymince.json.idump_into(filename, it)
        dumped = pymince.json.load_from(filename)

    assert dumped == ["a", "b"]


def test_dumped_string():
    with tempfile.TemporaryDirectory() as tmpdir:
        filename = os.path.join(tmpdir, "foo.json")
        pymince.json.idump_into(filename, "abcdfg")
        dumped = pymince.json.load_from(filename)

    assert dumped == ["a", "b", "c", "d", "f", "g"]


def test_dumped_empty():
    with tempfile.TemporaryDirectory() as tmpdir:
        filename = os.path.join(tmpdir, "foo.json")
        pymince.json.idump_into(filename, [])
        dumped = pymince.json.load_from(filename)
    assert dumped == []
