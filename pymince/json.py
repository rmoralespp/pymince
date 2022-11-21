import functools
import json
import zipfile

dumps = functools.partial(json.dumps, ensure_ascii=False)
dump = functools.partial(json.dump, ensure_ascii=False)
encoding = "utf-8"


def load_from(filename):
    """
    Load JSON from a file using "utf-8" encoding.

    Examples:
        from pymince.json import load_from

        dictionary = load_from("foo.json")
    """
    with open(filename, encoding=encoding) as file:
        return json.load(file)


def dump_into(filename, payload, indent=None):
    """
    Dump JSON to a file using "utf-8" encoding.

    Examples:
        from pymince.json import dump_into

        dump_into("foo.json", {"key": "value"})
    """
    with open(filename, "wt", encoding=encoding) as file:
        dump(payload, file, indent=indent)


def dump_into_zip(zip_path, arcname, payload, indent=None):
    """
    Dump JSON into the zip archive under the name arcname.

    Examples:
        from pymince.json import dump_into_zip

        dump_into_zip("archive.zip", "foo.json", {"key": "value"})
    """
    with zipfile.ZipFile(zip_path, mode="w") as zf:
        json_string = dumps(payload, indent=indent)
        zf.writestr(arcname, json_string)


def load_from_zip(zip_path, arcname):
    """
    Load JSON from a file named "arcname" inside a zip archive.

    Examples:
        from pymince.json import load_from_zip

        dictionary = load_from_zip("archive.zip", "foo.json")
    """
    with zipfile.ZipFile(zip_path, mode="r") as zf:
        with zf.open(arcname) as file:
            return json.load(file)
