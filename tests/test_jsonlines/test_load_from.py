# -*- coding: utf-8 -*-

import os
import tempfile

import pytest

import pymince.iterator
import pymince.jsonlines as jsonl


def test_load_from_without_lines():
    expected = ()
    with tempfile.TemporaryDirectory() as tmpdir:
        filename = os.path.join(tmpdir, "foo.json")
        with open(filename, mode='w', encoding='utf-8') as f:
            f.write("")
        result = tuple(jsonl.load_from(filename))
        assert result == expected


def test_load_from_with_many_lines():
    expected = (
        {"en": "Afghanistan", "es": "Afganistán"},
        {"en": "Albania", "es": "Albania"},
    )
    with tempfile.TemporaryDirectory() as tmpdir:
        filename = os.path.join(tmpdir, "foo.json")

        with open(filename, mode='w', encoding='utf-8') as f:
            f.write('{"en": "Afghanistan", "es": "Afganistán"}\n{"en": "Albania", "es": "Albania"}\n')

        result = tuple(jsonl.load_from(filename))
        assert result == expected


def test_load_from_with_not_found():
    with pytest.raises(FileNotFoundError):
        pymince.iterator.consume_all(jsonl.load_from("foo.json"))
