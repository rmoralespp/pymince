import os.path
import tempfile

import pymince.file


def test_make_directory_if_not_exists():
    with tempfile.TemporaryDirectory() as tmpdir:
        expected = os.path.join(tmpdir, "myDirectory")
        pymince.file.ensure_directory(expected)
        assert os.path.exists(expected)


def test_ignore_if_directory_already_exists():
    with tempfile.TemporaryDirectory() as tmpdir:
        expected = os.path.join(tmpdir, "myDirectory")
        os.makedirs(expected)
        pymince.file.ensure_directory(expected)
        assert os.path.exists(expected)


def test_ignore_if_file_already_exists():
    with tempfile.TemporaryDirectory() as tmpdir:
        # prepare
        expected = os.path.join(tmpdir, "myFile")
        with open(expected, mode="w") as f:
            f.write("foo")
        # execute test function
        pymince.file.ensure_directory(expected)
        # perform asserts
        assert os.path.exists(expected)
        assert os.path.isfile(expected)

        with open(expected) as f:
            assert f.read() == "foo"


def test_cleaning_if_file_already_exists():
    with tempfile.TemporaryDirectory() as tmpdir:
        # prepare
        expected = os.path.join(tmpdir, "myFile")
        with open(expected, mode="w") as f:
            f.write("foo")
        # execute test function
        pymince.file.ensure_directory(expected, cleaning=True)
        # perform asserts
        assert os.path.exists(expected)
        assert os.path.isdir(expected)


def test_cleaning_if_directory_already_exists():
    with tempfile.TemporaryDirectory() as tmpdir:
        # prepare
        expected = os.path.join(tmpdir, "myDirectory")
        os.makedirs(expected)
        with open(os.path.join(expected, "nestedFile"), mode="w") as nf:
            nf.write("foo")
        # execute test function
        pymince.file.ensure_directory(expected, cleaning=True)
        # perform asserts
        assert os.path.exists(expected)
        assert os.path.isdir(expected)
        assert pymince.file.is_empty_directory(expected)
