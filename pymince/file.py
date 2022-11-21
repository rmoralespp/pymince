import contextlib
import io
import os
import re
import shutil
import zipfile


@contextlib.contextmanager
def open_from_zip(zip_file, filename, mode="r"):
    """
    Open a file that is inside a zip file
    using "utf-8" encoding.

    :param zip_file: instance of ZipFile class
    :param str filename:
    :param str mode: Required opening zip modes "r" or "w"'. Default reading mode

    Examples:
    -------------------------------------------------
    import zipfile
    from pymince.file import open_from_zip

    with zipfile.ZipFile(zip_filename) as zf:
        # example1
        with open_from_zip(zf, "foo1.txt") as fd1:
            foo1_string = fd1.read()
        # example2
        with open_from_zip(zf, "foo2.txt") as fd2:
            foo2_string = fd2.read()
    -------------------------------------------------
    """
    with zip_file.open(filename, mode=mode) as fd:
        yield io.TextIOWrapper(fd, encoding="utf-8")


def match_from_zip(zip_file, pattern):
    """
    Make an iterator that returns file names in the zip file that
    match the given pattern.
    Uppercase/lowercase letters are ignored.

    :param zip_file: ZipFile object or zip path.
    :param pattern: "re.Pattern" to filter filename list
    :return: Iterator with the filenames found

    Examples:
        import pymince.file
        pymince.file.match_from_zip("archive.zip", "^file") # --> file1.log file2.txt
        pymince.file.match_from_zip(zipfile.ZipFile("archive.zip"), "^file") # --> file1.log file2.txt
    """

    def match(file):
        apply = re.compile(pattern, re.IGNORECASE).match
        return iter(filter(apply, file.namelist()))

    if isinstance(zip_file, zipfile.ZipFile):
        return match(zip_file)
    else:
        if isinstance(zip_file, str):
            with zipfile.ZipFile(zip_file) as zf:
                return match(zf)
        else:
            raise ValueError(zip_file)


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


def replace_extension(filename, old_ext=None, new_ext=None):
    """
    Replace filename "old_ext" with "new_ext"

    :param str filename:
    :param Optional[str] old_ext:
    :param Optional[str] new_ext:

    Examples:
        from pymince.file import replace_extension

        # remove extensions
        replace_extension("/home/user/file.old") # --> "/home/user/file"
        replace_extension("/home/user/file.old", old_ext=".old") # --> "/home/user/file"
        replace_extension("/home/user/file.old", old_ext=".new") # --> "/home/user/file.old"

        # replace extensions
        replace_extension("/home/user/file.old", new_ext=".new") # --> "/home/user/file.new"
        replace_extension("/home/user/file.old", old_ext=".old", new_ext=".new") # --> "/home/user/file.new"
        replace_extension("/home/user/file.old", old_ext=".new", new_ext=".new") # --> "/home/user/file.old"
    """

    root, ext = os.path.splitext(filename)  # Split the path in root and ext pair
    if old_ext is None or old_ext == ext:
        return root + (new_ext or "")
    else:
        return filename
