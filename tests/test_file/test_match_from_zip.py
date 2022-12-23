# -*- coding: utf-8 -*-
import os
import shutil
import tempfile
import zipfile

import pytest

import pymince.file
import tests

basename1 = "file1.log"
basename2 = "file2.log"
basename3 = "unexpected.log"


def make_files(directory):
    tests.make_file(os.path.join(directory, basename1))
    tests.make_file(os.path.join(directory, basename2))
    tests.make_file(os.path.join(directory, basename3))


def test_match_using_file():
    with tempfile.TemporaryDirectory() as tmpdir:
        make_files(tmpdir)
        zip_path = shutil.make_archive(tmpdir, "zip", root_dir=tmpdir)
        with zipfile.ZipFile(zip_path) as zp:
            result = pymince.file.match_from_zip(zp, "^file")
            assert sorted(result) == sorted((basename1, basename2))


def test_match_using_path():
    with tempfile.TemporaryDirectory() as tmpdir:
        make_files(tmpdir)
        zip_path = shutil.make_archive(tmpdir, "zip", root_dir=tmpdir)
        result = pymince.file.match_from_zip(zip_path, "^file")
        assert sorted(result) == sorted((basename1, basename2))


def test_match_with_value_error():
    with pytest.raises(ValueError):
        pymince.file.match_from_zip(object(), "^file")
