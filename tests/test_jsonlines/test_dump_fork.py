# -*- coding: utf-8 -*-

import os
import tempfile

import pytest

import pymince.jsonlines as jsonl
import tests.test_jsonlines as tests_jsonl


def read(p):
    with open(p, encoding="utf-8") as f:
        return f.read()


def test_dumped_iter_data():
    with tempfile.TemporaryDirectory() as tmp:
        foo_path = os.path.join(tmp, "foo.jsonl")
        var_path = os.path.join(tmp, "var.jsonl")
        baz_path = os.path.join(tmp, "baz.jsonl")

        path_items = (
            (foo_path, iter(tests_jsonl.sample_data)),
            (foo_path, ({"extra": True},)),
            (var_path, iter(tests_jsonl.sample_data)),
            (baz_path, iter(())),
        )

        jsonl.dump_fork(iter(path_items))

        assert read(foo_path) == '{"foo": 1}\n{"ño": 2}\n{"extra": true}'
        assert read(var_path) == '{"foo": 1}\n{"ño": 2}'
        assert read(baz_path) == ''


@pytest.mark.parametrize("dump_if_empty", (True, False))
def test_dumped_empty_data(dump_if_empty):
    with tempfile.TemporaryDirectory() as tmp:
        path = os.path.join(tmp, "foo.jsonl")
        path_items = ((path, ()),)
        jsonl.dump_fork(iter(path_items), dump_if_empty=dump_if_empty)
        if dump_if_empty:
            assert read(path) == ''
        else:
            assert not os.path.exists(path)
