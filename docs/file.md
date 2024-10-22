# File
Common file operations.

**decompress**
```
decompress(src_path, dst_path, size=65536)

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
```
**ensure_directory**
```
ensure_directory(path, cleaning=False)

Make sure the given file path is an existing directory.
If it does not exist, a new directory will be created.

:param str path:
:param bool cleaning:
    If "cleaning" is True and a directory already exists,
    this directory and the files contained in it will be deleted.

    If "cleaning" is True and a file already exists,
    this file will be deleted.
```
**get_valid_filename**
```
get_valid_filename(s)

Returns a valid filename for the given string.

- Remove leading/trailing spaces
- Change spaces to underscores
- Remove anything that is not an alphanumeric, dash, underscore, or dot
```
**is_empty_directory**
```
is_empty_directory(path)

Check if the given path is an empty directory.
```
**match_from_zip**
```
match_from_zip(zip_file, pattern)

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
```
**replace_extension**
```
replace_extension(filename, old_ext=None, new_ext=None)

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
```
**xopen**
```
xopen(name, mode='rb', encoding=None)

Open compressed files in Python based on their file extension.

- Supports compression formats: gzip => (.gz), bzip2 => (.bz2), xz => (.xz)
- If the file extension is not recognized, the file will be opened without compression.
- When text mode is required, UTF-8 encoding is used by default.
```