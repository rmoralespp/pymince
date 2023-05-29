# -*- coding: utf-8 -*-

import pymince.jsonlines as jsonl

data = (
    {"name": "foo", "age": 12},
    {"name": "abc", "age": 11},
)


def test_dumps_empty():
    assert jsonl.dumps(()) == ""


def test_dumps_many():
    expected = '{"name": "foo", "age": 12}\n{"name": "abc", "age": 11}\n'
    assert jsonl.dumps(iter(data)) == expected


def test_dumps_many_with_kwargs():
    expected = '{\n "name": "foo",\n "age": 12\n}\n{\n "name": "abc",\n "age": 11\n}\n'
    assert jsonl.dumps(iter(data), indent=1) == expected
