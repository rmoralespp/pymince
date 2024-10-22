# -*- coding: utf-8 -*-

"""Common file operations."""

import bz2
import functools
import gzip
import lzma
import os
import re
import shutil
import zipfile

import pymince._constants


def xopen(name, mode="rb", encoding=None):
    """
    Open compressed files in Python based on their file extension.

    - Supports compression formats: gzip => (.gz), bzip2 => (.bz2), xz => (.xz)
    - If the file extension is not recognized, the file will be opened without compression.
    - When text mode is required, UTF-8 encoding is used by default.
    """

    openers = {
        ".gz": gzip.open,
        ".bz2": bz2.open,
        ".xz": lzma.open,
    }

    ext = os.path.splitext(name)[1]
    fn = openers.get(ext, open)
    encoding = (encoding or pymince._constants.utf_8) if "t" in mode else None  # Text mode encoding is required.
    return fn(name, mode=mode, encoding=encoding)


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
    elif isinstance(zip_file, str):
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
    """Check if the given path is an empty directory."""

    return os.path.exists(path) and not os.path.isfile(path) and not os.listdir(path)


def replace_extension(filename, old_ext=None, new_ext=None):
    """
    Replace filename "old_ext" with "new_ext".

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


def decompress(src_path, dst_path, size=64 * 1024):
    """
    Decompress the given compressed file in blocks based on its extension format.
    Supports compression formats: gzip ⇒ (.gz), bzip2 ⇒ (.bz2), xz ⇒ (.xz)

    :param str src_path: Source file path
    :param str dst_path: Destination file(unzipped) path
    :param int size: Read up-to-size bytes from "src_path" for each block. Default is 64KB.
    :return: Destination file path

     Examples:
        from pymince.file import decompress

        decompress("/foo/src.txt.gz", "/baz/dst.txt")   # → "/baz/dst.txt"
        decompress("/foo/src.txt.bz2", "/baz/dst.txt")  # → "/baz/dst.txt"
        decompress("/foo/src.txt.xz", "/baz/dst.txt")   # → "/baz/dst.txt"
    """

    with xopen(src_path, mode="rb") as src, open(dst_path, mode="wb") as dst:
        lines = iter(functools.partial(src.read, size), b"")
        dst.writelines(lines)
    return dst_path


def get_valid_filename(s):
    """
    Returns a valid filename for the given string.

    - Remove leading/trailing spaces
    - Change spaces to underscores
    - Remove anything that is not an alphanumeric, dash, underscore, or dot
    """

    filename = re.sub(r"(?u)[^-\w.]", "", s.strip().replace(" ", "_"))
    if filename in ("", ".", ".."):
        raise ValueError(filename)
    return filename
