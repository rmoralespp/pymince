# -*- coding: utf-8 -*-
import shutil
import tempfile

import pymince.file
import pymince.json


def test_dumped_file():
    with tempfile.TemporaryDirectory() as tmpdir:
        archive = shutil.make_archive(tmpdir, "zip", root_dir=tmpdir)
        arcname = "foo.json"
        pymince.json.dump_into_zip(archive, arcname, {})
        matched = next(pymince.file.match_from_zip(archive, arcname))

    assert matched == arcname


def test_dumped_data():
    data = {"key": "ñó", "nested": [1, 2, 3]}
    with tempfile.TemporaryDirectory() as tmpdir:
        archive = shutil.make_archive(tmpdir, "zip", root_dir=tmpdir)
        arcname = "foo.json"

        pymince.json.dump_into_zip(archive, arcname, data)
        dumped = pymince.json.load_from_zip(archive, arcname)

    assert dumped == data
