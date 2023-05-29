# -*- coding: utf-8 -*-

import pymince.jsonlines as jsonl


def test_empty():
    assert tuple(jsonl.dumper(())) == ()


def test_many():
    data = (
        {"languages": {"ara": "Arabic"}},
        {"languages": {"srp": "Serbian"}},
    )

    expected = ('{"languages": {"ara": "Arabic"}}', '\n', '{"languages": {"srp": "Serbian"}}', '\n')
    result = jsonl.dumper(data)
    assert tuple(result) == expected
