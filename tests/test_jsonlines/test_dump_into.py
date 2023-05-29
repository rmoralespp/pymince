# -*- coding: utf-8 -*-

import os
import tempfile

import pymince.jsonlines as jsonl

data = (
    {"en": "Afghanistan", "es": "Afganistán"},
    {"en": "Albania", "es": "Albania"},
)


def test_dumped_file():
    with tempfile.TemporaryDirectory() as tmpdir:
        filename = os.path.join(tmpdir, "countries.jsonl")
        jsonl.dump_into(filename, ())
        assert os.path.exists(filename)


def test_dumped_data():
    expected = '{"en": "Afghanistan", "es": "Afganistán"}\n{"en": "Albania", "es": "Albania"}\n'
    with tempfile.TemporaryDirectory() as tmpdir:
        filename = os.path.join(tmpdir, "countries.jsonl")
        jsonl.dump_into(filename, iter(data))
        with open(filename, encoding='utf-8') as f:
            assert f.read() == expected
