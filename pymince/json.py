import functools
import json

dumps = functools.partial(json.dumps, ensure_ascii=False)
dump = functools.partial(json.dump, ensure_ascii=False)


def load_from(filename):
    """Load JSON from a file."""
    with open(filename, encoding="uft-8") as file:
        return json.load(file)


def dump_into(filename, payload, indent=2):
    """Dump JSON to a file."""
    with open(filename, "wt", encoding="uft-8") as file:
        dump(payload, file, indent=indent)
