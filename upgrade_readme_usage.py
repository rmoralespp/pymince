import inspect
import itertools
import logging
import os
import re

import pymince.algorithm
import pymince.boolean
import pymince.dates
import pymince.dictionary
import pymince.file
import pymince.functional
import pymince.iterator
import pymince.json
import pymince.logging
import pymince.retry
import pymince.std
import pymince.text
import pymince.warnings
import pymince.xml

modules = (
    pymince.algorithm,
    pymince.boolean,
    pymince.dates,
    pymince.dictionary,
    pymince.file,
    pymince.functional,
    pymince.iterator,
    pymince.json,
    pymince.logging,
    pymince.retry,
    pymince.std,
    pymince.text,
    pymince.warnings,
    pymince.xml,
)


def cleandoc(obj):
    docstring = obj.__doc__
    docstring = inspect.cleandoc(docstring) if docstring else ''
    return docstring


def member2markdown(member):
    name = member.__name__
    docstring = cleandoc(member)

    try:
        signature = inspect.signature(member)
    except ValueError:
        signature = ()

    lines = (
        f"##### {member.__name__}",
        "```",
        f"{name}{signature}",
        "",
        f"{docstring}",
        "```",
    )
    return "\n".join(lines)


def getmembers(module):
    def filtering(n):
        return (inspect.isclass(n) or inspect.isfunction(n))
    yield from inspect.getmembers(module, filtering)


def module2markdown(module):
    def members2markdown():
        for _name, member in getmembers(module):
            yield member2markdown(member)

    module_name = os.path.basename(module.__file__)
    module_desc = cleandoc(module)

    lines = itertools.chain((f"\n#### {module_name}\n{module_desc}",), members2markdown())
    return "\n".join(lines)


def make_table():
    """
    | Modules | Tools |
    | -----:  | ----: |
    | dictionary.py   | [from_objects](#from_objects), [frozendict](#frozendict) |
    | file.py         | [ensure_directory](#ensure_directory) |
    """

    header = "| PyModules  | Tools  |"
    border = "| :--------  | :----- |"
    table = [header, border]
    for module in modules:
        row = ""
        module_name = os.path.basename(module.__file__)
        row += f"| **{module_name}** |"
        row += ", ".join((f"[*{m.__name__}*](#{m.__name__})" for _, m in getmembers(module)))
        row += "|"
        table.append(row)
    table = "\n".join(table)
    return table


if __name__ == "__main__":
    base_dir = os.path.dirname(os.path.basename(__file__))
    readme_path = os.path.join(base_dir, "README.md")

    pattern = re.compile(r"### Usage.*(?=###)", flags=re.DOTALL)

    content_title = "### Usage"
    content_table = make_table()
    content_items = "".join(module2markdown(module) for module in modules)

    content_lines = (
        content_title,
        content_table,
        content_items,
        "",  # ensure last \n
    )
    content = "\n".join(content_lines)

    with open(readme_path, encoding="utf-8") as f:
        old_string = f.read()
        new_string = pattern.sub(content, old_string)

    if new_string != old_string:
        logging.basicConfig(level=logging.DEBUG)
        with pymince.logging.timed_block("upgrade_readme_usage"):
            with open(readme_path, mode="w", encoding="utf-8") as f:
                f.write(new_string)
