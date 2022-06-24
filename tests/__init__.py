def make_file(filename, content=""):
    with open(filename, mode="wt") as f:
        f.write(content)
    return filename
