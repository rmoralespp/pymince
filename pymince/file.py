import contextlib
import io
import os
import re
import shutil


@contextlib.contextmanager
def open_on_zip(zip_file, filename):
    """
    Open a file that is inside a zip file.

    Usage:
    -------------------------------------------------
    import zipfile
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
    match = re.compile(pattern, re.IGNORECASE).match
    return filter(match, zip_file.namelist())


def ensure_directory(path, cleaning=False):
    if os.path.exists(path):
        if cleaning:
            shutil.rmtree(path)
            os.makedirs(path)
    else:
        os.makedirs(path)
