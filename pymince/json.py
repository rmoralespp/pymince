import functools
import json

dumps = functools.partial(json.dumps, ensure_ascii=False)
dump = functools.partial(json.dump, ensure_ascii=False)


def load_from(filename):
    """
    Load JSON from a file.

    Usage:
        from pymince.json import load_from

        dictionary = load_from("foo.json")
    """
    with open(filename, encoding="utf-8") as file:
        return json.load(file)


def dump_into(filename, payload, indent=2):
    """
    Dump JSON to a file.

    Usage:
        from pymince.json import dump_into

        dump_into("foo.json", {"key": "value"})
    """
    with open(filename, "wt", encoding="utf-8") as file:
        dump(payload, file, indent=indent)
