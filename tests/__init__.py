# -*- coding: utf-8 -*-


def make_file(filename, content=""):
    with open(filename, mode="w", encoding="utf-8") as f:
        f.write(content)
    return filename
