# -*- coding: utf-8 -*-

import os
import tempfile

import pytest

import pymince.json


def read(p):
    with open(p, encoding="utf-8") as f:
        return f.read()


def test_dumped_iter_data():
    with tempfile.TemporaryDirectory() as tmp:
        foo_path = os.path.join(tmp, "foo.json")
        var_path = os.path.join(tmp, "var.json")
        baz_path = os.path.join(tmp, "baz.json")

        path_items = (
            (
                foo_path,
                iter(
                    (
                        {"a": 1},
                        {"b": 2},
                    ),
                ),
            ),
            (foo_path, ({"c": 3},)),
            (
                var_path,
                iter(
                    (
                        {"a": 1},
                        {"b": 2},
                    ),
                ),
            ),
            (baz_path, iter(())),
        )

        pymince.json.idump_fork(iter(path_items))

        assert read(foo_path) == '[\n{"a": 1},\n{"b": 2},\n{"c": 3}\n]'
        assert read(var_path) == '[\n{"a": 1},\n{"b": 2}\n]'
        assert read(baz_path) == '[\n]'


@pytest.mark.parametrize("dump_if_empty", (True, False))
def test_dumped_empty_data(dump_if_empty):
    with tempfile.TemporaryDirectory() as tmp:
        path = os.path.join(tmp, "foo.json")
        path_items = ((path, ()),)
        pymince.json.idump_fork(iter(path_items), dump_if_empty=dump_if_empty)
        if dump_if_empty:
            assert read(path) == '[\n]'
        else:
            assert not os.path.exists(path)
