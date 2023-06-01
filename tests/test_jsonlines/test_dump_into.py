# -*- coding: utf-8 -*-

import os
import tempfile

import pymince.jsonlines as jsonl
import tests.test_jsonlines as tests_jsonl


def test_exists_file():
    with tempfile.TemporaryDirectory() as tmp:
        path = os.path.join(tmp, "foo.jsonl")
        jsonl.dump_into(path, ())
        assert os.path.exists(path)


def test_dumped_iter_data():
    with tempfile.TemporaryDirectory() as tmp:
        path = os.path.join(tmp, "foo.jsonl")
        jsonl.dump_into(path, iter(tests_jsonl.sample_data))
        with open(path, encoding="utf-8") as f:
            assert f.read() == tests_jsonl.sample_text
