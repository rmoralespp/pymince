# -*- coding: utf-8 -*-

import pymince.jsonlines as jsonl
import tests.test_jsonlines as tests_jsonl


def test_empty():
    assert tuple(jsonl.dumper(())) == ()


def test_no_empty():
    result = jsonl.dumper(tests_jsonl.sample_data)
    assert tuple(result) == tests_jsonl.sample_lines
