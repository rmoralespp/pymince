# -*- coding: utf-8 -*-
import os
import tempfile

import pymince.json


def test_dumped_file():
    with tempfile.TemporaryDirectory() as tmpdir:
        filename = os.path.join(tmpdir, "foo.json")
        pymince.json.dump_into(filename, {})
        assert os.path.exists(filename)


def test_dumped_data():
    data = {"key": "ñó", "nested": [1, 2, 3]}
    with tempfile.TemporaryDirectory() as tmpdir:
        filename = os.path.join(tmpdir, "foo.json")
        pymince.json.dump_into(filename, data)
        dumped = pymince.json.load_from(filename)

    assert dumped == data
