import contextlib
import io
import os
import re
import shutil


@contextlib.contextmanager
def open_on_zip(zip_file, filename):
    """
    Open a file that is inside a zip file.

    :param zip_file: instance of ZipFile class
    :param str filename:

    Usage:
    -------------------------------------------------
    import zipfile
    from pymince.file import open_on_zip

    with zipfile.ZipFile(zip_filename) as zf:
        # example1
        with open_on_zip(zf, "foo1.txt") as fd1:
            foo1_string = fd1.read()
        # example2
        with open_on_zip(zf, "foo2.txt") as fd2:
            foo2_string = fd2.read()
    -------------------------------------------------
    """
    with zip_file.open(filename) as fd:
        yield io.TextIOWrapper(fd, encoding="utf-8")


def match_on_zip(zip_file, pattern):
    """
    Make an iterator that returns file names in the zip file that
    match the given pattern.

    :param zip_file: instance of ZipFile class
    :param pattern: Callable to filter filename list
    """
    matcher = re.compile(pattern, re.IGNORECASE).match
    return iter(filter(matcher, zip_file.namelist()))


def ensure_directory(path, cleaning=False):
    """
    Make sure the given file path is an existing directory.
    If it does not exist, a new directory will be created.

    :param str path:
    :param bool cleaning:
        If "cleaning" is True and the directory already exists,
        existing content will be deleted.
    """
    if os.path.exists(path):
        if cleaning:
            shutil.rmtree(path)
            os.makedirs(path)
    else:
        os.makedirs(path)
