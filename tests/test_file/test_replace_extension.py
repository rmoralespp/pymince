import pymince.file


def test_remove_if_equals_extensions():
    filename = "/home/User/Desktop/file.txt"
    expected = "/home/User/Desktop/file"
    assert pymince.file.replace_extension(filename, old_ext=".txt") == expected


def test_remove_if_not_given_old_extension():
    filename = "/home/User/Desktop/file.txt"
    expected = "/home/User/Desktop/file"
    assert pymince.file.replace_extension(filename) == expected


def test_ignore_if_given_filename_has_not_extension():
    expected = "/home/User/Desktop/file"
    assert pymince.file.replace_extension(expected, old_ext=".txt") == expected


def test_ignore_if_mismatching_extensions():
    expected = "/home/User/Desktop/file.txt"
    assert pymince.file.replace_extension(expected, old_ext=".py") == expected


def test_replace_extension_if_equals_extensions():
    filename = "/home/User/Desktop/file.txt"
    expected = "/home/User/Desktop/file.xls"
    assert pymince.file.replace_extension(filename, old_ext=".txt", new_ext=".xls") == expected


def test_replace_if_not_given_old_extension():
    filename = "/home/User/Desktop/file.txt"
    expected = "/home/User/Desktop/file.xls"
    assert pymince.file.replace_extension(filename, new_ext=".xls") == expected


def test_replace_extension_with_many_dot():
    filename = "/home/User/Desktop/file.file.txt"
    expected = "/home/User/Desktop/file.file.doc"
    assert pymince.file.replace_extension(filename, old_ext=".txt", new_ext=".doc") == expected
