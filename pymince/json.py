import csv
import functools
import itertools
import json
import operator
import zipfile

dumps = functools.partial(json.dumps, ensure_ascii=False)
dump = functools.partial(json.dump, ensure_ascii=False)
ENCODING = "utf-8"


def load_from(filename, encoding=ENCODING):
    """
    Load JSON from a file using "utf-8" encoding.

    Examples:
        from pymince.json import load_from

        dictionary = load_from("foo.json")
    """
    with open(filename, encoding=encoding) as file:
        return json.load(file)


def dump_into(filename, payload, indent=None, encoding=ENCODING):
    """
    Dump JSON to a file using "utf-8" encoding.

    Examples:
        from pymince.json import dump_into

        dump_into("foo.json", {"key": "value"})
    """
    with open(filename, "w", encoding=encoding) as file:
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


def dump_from_csv(
        csv_path,
        json_path,
        /,
        *,
        fieldnames=None,
        indent=None,
        start=0,
        stop=None,
        strip=True,
        encoding=ENCODING,
):
    """
    Dump CSV file to a JSON file using "utf-8" encoding.

    :param str csv_path:
    :param str json_path:
    :param fieldnames: list of keys for the JSON
    :param str indent: JSON indent
    :param int start:
        If start is specified, will skip all preceding elements;
        otherwise, start defaults to zero.
    :param int stop:
    :param bool strip:
        Whether or not white space should be removed from the
        beginning and end of field values.
    :param str encoding: utf-8 is used by default.
    """

    def read():
        reader = csv.DictReader(csv_f, fieldnames=fieldnames)
        if strip:
            apply = operator.methodcaller('strip')
            for row in reader:
                yield {k and apply(k): (apply(v) if isinstance(v, str) else v) for k, v in row.items()}
        else:
            yield from reader

    with open(csv_path, encoding=encoding, newline='') as csv_f:
        # The official csv doc recommends opening the file with newline='' on all platforms to disable
        # universal newlines translation.

        data = itertools.islice(read(), start, stop)
        pool = tuple(data)

    dump_into(json_path, pool, indent=indent, encoding=encoding)
