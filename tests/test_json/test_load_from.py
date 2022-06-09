import os
import tempfile

import pytest

import pymince.json


def test_load_from():
    data = {"key": "ñó", "nested": [1, 2, 3]}
    with tempfile.TemporaryDirectory() as tmpdir:
        filename = os.path.join(tmpdir, "foo.json")
        pymince.json.dump_into(filename, data)
        loaded = pymince.json.load_from(filename)
    assert loaded == data


def test_load_from_with_not_found():
    with pytest.raises(FileNotFoundError):
        pymince.json.load_from("foo.json")
