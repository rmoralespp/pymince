# -*- coding: utf-8 -*-

import os
import tempfile

import pytest

import pymince.iterator
import pymince.jsonlines as jsonl
import tests
import tests.test_jsonlines as tests_jsonl


def test_load_empty():
    with tempfile.TemporaryDirectory() as tmp:
        path = os.path.join(tmp, "foo.jsonl")
        tests.make_file(path, "")
        assert tuple(jsonl.load_from(path)) == ()


def test_load_data():
    with tempfile.TemporaryDirectory() as tmp:
        path = os.path.join(tmp, "foo.jsonl")
        tests.make_file(path, tests_jsonl.sample_text)
        result = tuple(jsonl.load_from(path))
        assert result == tests_jsonl.sample_data


def test_file_not_found():
    with pytest.raises(FileNotFoundError):
        pymince.iterator.consume_all(jsonl.load_from("jsonl.json"))
