# -*- coding: utf-8 -*-

import inspect
import itertools
import os

import ruamel.yaml

import pymince.algorithm
import pymince.benchmark
import pymince.boolean
import pymince.dates
import pymince.dictionary
import pymince.file
import pymince.functional
import pymince.iterator
import pymince.json
import pymince.logging
import pymince.std
import pymince.text
import pymince.warnings
import pymince.xml
import pymince.patterns

modules = (
    pymince.algorithm,
    pymince.benchmark,
    pymince.boolean,
    pymince.dates,
    pymince.dictionary,
    pymince.file,
    pymince.functional,
    pymince.iterator,
    pymince.json,
    pymince.logging,
    pymince.patterns,
    pymince.std,
    pymince.text,
    pymince.warnings,
    pymince.xml,
)


def cleandoc(obj):
    docstring = obj.__doc__
    docstring = inspect.cleandoc(docstring) if docstring else ""
    return docstring


def member2md(member):
    name = member.__name__
    docstring = cleandoc(member)

    try:
        signature = inspect.signature(member)
    except ValueError:
        signature = ()

    lines = (
        f"**{member.__name__}**",
        "```",
        f"{name}{signature}",
        "",
        f"{docstring}",
        "```",
    )
    return "\n".join(lines)


def getmembers(module):
    def filtering(n):
        name = getattr(n, "__name__", None)
        if name and name.startswith("_"):
            return False
        else:
            return inspect.isclass(n) or inspect.isfunction(n)

    yield from inspect.getmembers(module, filtering)


def module2md(module):
    def members2markdown():
        for _name, member in getmembers(module):
            yield member2md(member)

    module_name, _ = os.path.splitext(os.path.basename(module.__file__))
    module_desc = cleandoc(module)

    lines = itertools.chain((f"# {module_name.capitalize()}", module_desc, ""), members2markdown())
    return (module_name, "\n".join(lines))


if __name__ == "__main__":
    base_dir = os.path.dirname(os.path.basename(__file__))
    mkdocs_path = os.path.join(base_dir, "mkdocs.yml")
    dir_docs = os.path.join(base_dir, "docs")
    index_path = os.path.join(dir_docs, "index.md")

    api_usage = []
    nav = [
        {"Introduction": "index.md"},
        {"Api usage": api_usage},
    ]

    mkdocs_data = {
        "site_name": "pymince",
        "site_description": "Documentation for the pymince Python library",
        "site_url": "https://github.com/rmoralespp/pymince",
        "repo_url": "https://github.com/rmoralespp/pymince",
        "repo_name": "pymince",
        "theme": {
            "name": "readthedocs",
            "custom_dir": 'docs',
        },
        "nav": nav,
    }

    for module in modules:
        name, content = module2md(module)
        module_path = os.path.join(dir_docs, f"{name}.md")
        api_usage.append({f"{name.capitalize()} utils": f"{name}.md"})
        with open(module_path, "w", encoding="utf-8") as f:
            f.write(content)

    yaml = ruamel.yaml.YAML()
    with open(mkdocs_path, 'w', encoding="utf-8") as file:
        yaml.dump(mkdocs_data, file)
