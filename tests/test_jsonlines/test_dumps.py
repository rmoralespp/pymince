# -*- coding: utf-8 -*-

import pymince.jsonlines as jsonl
import tests.test_jsonlines as tests_jsonl


def test_dumps_empty():
    assert not jsonl.dumps(())


def test_dumps_data():
    result = jsonl.dumps(iter(tests_jsonl.sample_data))
    assert result == tests_jsonl.sample_text
