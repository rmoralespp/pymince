import shutil
import tempfile

import pytest

import pymince.json


def test_load_from():
    data = {"key": "ñó", "nested": [1, 2, 3]}
    with tempfile.TemporaryDirectory() as tmpdir:
        archive = shutil.make_archive(tmpdir, "zip", root_dir=tmpdir)
        arcname = "foo.json"
        pymince.json.dump_into_zip(archive, arcname, data)

        loaded = pymince.json.load_from_zip(archive, "foo.json")
    assert loaded == data


def test_load_from_with_not_found():
    with pytest.raises(FileNotFoundError):
        pymince.json.load_from_zip("archive.zip", "foo.json")
