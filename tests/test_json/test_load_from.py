# -*- coding: utf-8 -*-

import json
import os
import tempfile

import pytest

import pymince.json
import pymince._constants
import pymince.file

EXTENSIONS = (".json.gz", ".json.bz2", ".json.xz", ".json")


@pytest.mark.parametrize("extension", EXTENSIONS)
def test_load_given_filepath(extension):
    expected = data = {"key": "ñó", "nested": [1, 2, 3]}
    with tempfile.TemporaryDirectory() as tmp:
        path = os.path.join(tmp, f"foo{extension}")
        with pymince.file.xopen(path, mode="wt", encoding=pymince._constants.utf_8) as fd:
            fd.write(json.dumps(data))
        result = pymince.json.load_from(path)
    assert result == expected


def test_load_from_with_not_found():
    with pytest.raises(FileNotFoundError):
        pymince.json.load_from("foo.json")
