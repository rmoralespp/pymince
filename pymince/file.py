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

    Examples:
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
    Uppercase/lowercase letters are ignored.

    :param zip_file: instance of ZipFile class
    :param pattern: "re.Pattern" to filter filename list
    :return: Iterator with the filenames found

    Examples:
        import pymince.file
        pymince.file.match_on_zip(zip_file, "^file") # --> file1.log file2.txt

    """
    matcher = re.compile(pattern, re.IGNORECASE).match
    return iter(filter(matcher, zip_file.namelist()))


def ensure_directory(path, cleaning=False):
    """
    Make sure the given file path is an existing directory.
    If it does not exist, a new directory will be created.

    :param str path:
    :param bool cleaning:
        If "cleaning" is True and a directory already exists,
        this directory and the files contained in it will be deleted.

        If "cleaning" is True and a file already exists,
        this file will be deleted.
    """
    if os.path.exists(path):
        if cleaning:
            if os.path.isdir(path):
                # Delete a directory and the files contained in it.
                shutil.rmtree(path)
            else:
                os.remove(path)  # Removes the specified file.
            os.makedirs(path)
    else:
        os.makedirs(path)


def is_empty_directory(path):
    """
    Function to check if the given path is an empty directory.

    :param str path:
    :rtype: bool
    """

    return os.path.exists(path) and not os.path.isfile(path) and not os.listdir(path)
