# -*- coding: utf-8 -*-

import os
import tempfile

import pytest

import pymince.json


def test_dumped_file():
    with tempfile.TemporaryDirectory() as tmpdir:
        filename = os.path.join(tmpdir, "foo.json")
        pymince.json.dump_into(filename, {})
        assert os.path.exists(filename)


@pytest.mark.parametrize("extension", pymince.json.EXTENSIONS)
def test_dumped_data(extension):
    data = {"key": "ñó", "nested": [1, 2, 3]}
    with tempfile.TemporaryDirectory() as tmpdir:
        filename = os.path.join(tmpdir, f"foo{extension}")
        pymince.json.dump_into(filename, data)
        dumped = pymince.json.load_from(filename)
    assert dumped == data
