import inspect
import itertools
import logging
import os
import re

import pymince.dictionary
import pymince.file
import pymince.iterator
import pymince.json
import pymince.logging
import pymince.retry
import pymince.std
import pymince.text

modules = (
    pymince.dictionary,
    pymince.file,
    pymince.iterator,
    pymince.json,
    pymince.logging,
    pymince.retry,
    pymince.std,
    pymince.text,
)


def cleandoc(obj):
    doctring = obj.__doc__
    doctring = inspect.cleandoc(doctring) if doctring else ''
    return doctring


def member2markdown(member):
    name = member.__name__
    doctring = cleandoc(member)

    lines = (
        f"##### {member.__name__}",
        "```",
        f"{name}{inspect.signature(member)}",
        "",
        f"{doctring}",
        "```",
    )
    return "\n".join(lines)


def getmembers(module):
    filtering = lambda n: inspect.isclass(n) or inspect.isfunction(n)
    yield from inspect.getmembers(module, filtering)


def module2markdown(module):
    def members2markdown():
        for name, member in getmembers(module):
            yield member2markdown(member)

    module_name = os.path.basename(module.__file__)
    docstring = cleandoc(module)
    docstring = docstring and f"*{docstring}*"

    lines = itertools.chain((f"\n#### {module_name} {docstring}",), members2markdown())
    return "\n".join(lines)


def make_table():
    """
    | dictionary | file | iterator |
    | ---------- | ---- | -------  |
    | a | b | b  |
    | d | e | f  |
    """

    table = []
    for module in modules:
        row = []
        header = os.path.basename(module.__file__)
        border = "-" * len(header) + ":"
        row.extend((header, border))
        for _, member in getmembers(module):
            name = member.__name__
            link = f"[{name}](#{name})"
            row.append(link)
        table.append(row)
    table = itertools.zip_longest(*table, fillvalue="")
    table = "\n".join("| " + " | ".join(row) + " |" for row in table)
    return table


if __name__ == "__main__":
    base_dir = os.path.dirname(os.path.basename(__file__))
    readme_path = os.path.join(base_dir, "README.md")

    pattern = re.compile(r"### Usage.*(?=###)", flags=re.DOTALL)
    content = "".join(module2markdown(module) for module in modules)
    content = "### Usage\n" + make_table() + "\n" + content + "\n"
    with open(readme_path, mode="r", encoding="utf-8") as f:
        old_string = f.read()
        new_string = pattern.sub(content, old_string)

    if new_string != old_string:
        logging.basicConfig(level=logging.DEBUG)
        with pymince.logging.timed_block("upgrade_readme_usage"):
            with open(readme_path, mode="wt", encoding="utf-8") as f:
                f.write(new_string)
