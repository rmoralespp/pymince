# -*- coding: utf-8 -*-

import io

import pymince.jsonlines as jsonl
import tests.test_jsonlines as tests_jsonl


def test_dump_text() -> None:
    fp = io.StringIO()
    jsonl.dump(iter(tests_jsonl.sample_data), fp)
    assert fp.getvalue() == tests_jsonl.sample_text
