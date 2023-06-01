# -*- coding: utf-8 -*-

import io
import json

import pytest

import pymince.iterator
import pymince.jsonlines as jsonl
import tests.test_jsonlines as tests_jsonl


def test_invalid_lines():
    result = jsonl.load(io.StringIO("[1, 2]\n\n[3]"))
    with pytest.raises(json.JSONDecodeError):
        pymince.iterator.consume_all(result)


def test_invalid_utf8() -> None:
    result = jsonl.load(io.BytesIO(b"\xff\xff"))
    with pytest.raises(UnicodeDecodeError):
        pymince.iterator.consume_all(result)


def test_load_empty():
    result = jsonl.load(io.StringIO())
    assert tuple(result) == ()


def test_load_data():
    result = jsonl.load(io.StringIO(tests_jsonl.sample_text))
    assert tuple(result) == tests_jsonl.sample_data
