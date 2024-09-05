# -*- coding: utf-8 -*-

import json
import os
import tempfile

import pytest

import pymince.json


@pytest.mark.parametrize("extension", pymince.json.EXTENSIONS)
def test_load_given_filepath(extension):
    expected = data = {"key": "ñó", "nested": [1, 2, 3]}
    with tempfile.TemporaryDirectory() as tmp:
        path = os.path.join(tmp, f"foo{extension}")
        with pymince.json.xopen(path, "wt", pymince.json.ENCODING) as fd:
            fd.write(json.dumps(data))
        result = pymince.json.load_from(path)
    assert result == expected


def test_load_from_with_not_found():
    with pytest.raises(FileNotFoundError):
        pymince.json.load_from("foo.json")
