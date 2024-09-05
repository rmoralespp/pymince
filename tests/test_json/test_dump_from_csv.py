# -*- coding: utf-8 -*-
import contextlib
import csv
import os
import tempfile

import pytest

import pymince.json

csv_head = [" col1", "col2 ", "co l3", " col4 "]
csv_rows = [
    [" ñoo", "var ", " !!! ", 123],
    [" baz", "foo ", " %6$ ", 567],
]


@contextlib.contextmanager
def temp_paths(extension):
    with tempfile.TemporaryDirectory() as tmpdir:
        csv_path = os.path.join(tmpdir, "foo.csv")
        json_path = os.path.join(tmpdir, f"foo{extension}")

        with open(csv_path, "w", newline="", encoding=pymince.json.ENCODING) as f:
            writer = csv.writer(f)
            writer.writerows([csv_head, *csv_rows])

        yield csv_path, json_path


@pytest.mark.parametrize("extension", pymince.json.EXTENSIONS)
def test_dumped_data(extension):
    expected = [
        {"co l3": "co l3", "col1": "col1", "col2": "col2", "col4": "col4"},
        {"co l3": "!!!", "col1": "ñoo", "col2": "var", "col4": "123"},
        {"co l3": "%6$", "col1": "baz", "col2": "foo", "col4": "567"},
    ]
    with temp_paths(extension) as (csv_path, json_path):
        pymince.json.dump_from_csv(csv_path, json_path, fieldnames=csv_head)
        dumped = pymince.json.load_from(json_path)
        assert dumped == expected


def test_dumped_data_excluding_header():
    expected = [
        {"co l3": "!!!", "col1": "ñoo", "col2": "var", "col4": "123"},
        {"co l3": "%6$", "col1": "baz", "col2": "foo", "col4": "567"},
    ]
    with temp_paths(".json") as (csv_path, json_path):
        pymince.json.dump_from_csv(csv_path, json_path, fieldnames=csv_head, start=1)
        dumped = pymince.json.load_from(json_path)
        assert dumped == expected


def test_dumped_data_excluding_header_and_footer():
    expected = [
        {"co l3": "!!!", "col1": "ñoo", "col2": "var", "col4": "123"},
    ]
    with temp_paths(".json") as (csv_path, json_path):
        pymince.json.dump_from_csv(csv_path, json_path, fieldnames=csv_head, start=1, stop=2)
        dumped = pymince.json.load_from(json_path)
        assert dumped == expected


def test_dumped_data_start_and_stop_equals():
    expected = []
    with temp_paths(".json") as (csv_path, json_path):
        pymince.json.dump_from_csv(csv_path, json_path, fieldnames=csv_head, start=1, stop=1)
        dumped = pymince.json.load_from(json_path)
        assert dumped == expected


def test_dumped_data_strip_false():
    expected = [
        {" col1": " col1", " col4 ": " col4 ", "co l3": "co l3", "col2 ": "col2 "},
        {" col1": " ñoo", " col4 ": "123", "co l3": " !!! ", "col2 ": "var "},
        {" col1": " baz", " col4 ": "567", "co l3": " %6$ ", "col2 ": "foo "},
    ]
    with temp_paths(".json") as (csv_path, json_path):
        pymince.json.dump_from_csv(csv_path, json_path, fieldnames=csv_head, strip=False)
        dumped = pymince.json.load_from(json_path)
        assert dumped == expected


def test_dumped_data_with_fieldnames():
    fieldnames = ["key1", "key2", "key3", "key4"]
    expected = [
        {"key1": "col1", "key2": "col2", "key3": "co l3", "key4": "col4"},
        {"key1": "ñoo", "key2": "var", "key3": "!!!", "key4": "123"},
        {"key1": "baz", "key2": "foo", "key3": "%6$", "key4": "567"},
    ]
    with temp_paths(".json") as (csv_path, json_path):
        pymince.json.dump_from_csv(csv_path, json_path, fieldnames=fieldnames)
        dumped = pymince.json.load_from(json_path)
        assert dumped == expected


def test_dumped_data_with_null_keys():
    fieldnames = ["key1", "key2"]
    expected = [
        {"key1": "col1", "key2": "col2", "null": ["co l3", " col4 "]},
        {"key1": "ñoo", "key2": "var", "null": [" !!! ", "123"]},
        {"key1": "baz", "key2": "foo", "null": [" %6$ ", "567"]},
    ]
    with temp_paths(".json") as (csv_path, json_path):
        pymince.json.dump_from_csv(csv_path, json_path, fieldnames=fieldnames)
        dumped = pymince.json.load_from(json_path)
        assert dumped == expected


def test_dumped_data_with_null_values():
    fieldnames = ["key1", "key2", "key3", "key4", "key5"]
    expected = [
        {"key1": "col1", "key2": "col2", "key3": "co l3", "key4": "col4", "key5": None},
        {"key1": "ñoo", "key2": "var", "key3": "!!!", "key4": "123", "key5": None},
        {"key1": "baz", "key2": "foo", "key3": "%6$", "key4": "567", "key5": None},
    ]
    with temp_paths(".json") as (csv_path, json_path):
        pymince.json.dump_from_csv(csv_path, json_path, fieldnames=fieldnames)
        dumped = pymince.json.load_from(json_path)
        assert dumped == expected


def test_dumped_data_with_empty_fields():
    expected = [
        {"null": [" col1", "col2 ", "co l3", " col4 "]},
        {"null": [" ñoo", "var ", " !!! ", "123"]},
        {"null": [" baz", "foo ", " %6$ ", "567"]},
    ]
    with temp_paths(".json") as (csv_path, json_path):
        pymince.json.dump_from_csv(csv_path, json_path, fieldnames=[])
        dumped = pymince.json.load_from(json_path)
        assert dumped == expected
