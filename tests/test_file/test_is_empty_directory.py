import os.path
import tempfile

import pymince.file
import tests.test_file


def test_is_empty_directory_true():
    with tempfile.TemporaryDirectory() as tmpdir:
        assert pymince.file.is_empty_directory(tmpdir)


def test_is_empty_directory_false_if_has_any_child_file():
    with tempfile.TemporaryDirectory() as tmpdir:
        tests.test_file.make_file(os.path.join(tmpdir, "foo"))
        assert not pymince.file.is_empty_directory(tmpdir)


def test_is_empty_directory_false_if_has_any_child_dir():
    with tempfile.TemporaryDirectory() as tmpdir:
        os.makedirs(os.path.join(tmpdir, "foo"))
        assert not pymince.file.is_empty_directory(tmpdir)


def test_is_empty_directory_false_if_path_is_file():
    with tempfile.TemporaryDirectory() as tmpdir:
        filename = tests.test_file.make_file(os.path.join(tmpdir, "foo"))
        assert not pymince.file.is_empty_directory(filename)
