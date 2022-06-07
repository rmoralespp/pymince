import inspect
import os

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
)


def member2markdown(member):
    name = member.__name__
    lines = (
        f"##### {name}",
        "```",
        f"{name}{inspect.signature(member)}",
        f"{member.__doc__ or ''}",
        "```",
    )
    return "\n".join(lines)


def module2markdown(module):
    def members2markdown():
        for name, member in inspect.getmembers(module, matcher):
            yield member2markdown(member)

    module_name = os.path.basename(module.__file__)
    matcher = lambda n: inspect.isclass(n) or inspect.isfunction(n)

    lines = (f"\n#### {module_name}",) + tuple(members2markdown())
    return "\n".join(lines)


if __name__ == "__main__":
    base_dir = os.path.dirname(os.path.basename(__file__))
    readme_path = os.path.join(base_dir, "README.md")
    content = "".join(module2markdown(module) for module in modules)
    with open(readme_path, mode="r", encoding="utf-8") as f:
        string = f.read()

    string = string.replace("__usage__", content)
    with open(readme_path, mode="wt", encoding="utf-8") as f:
        f.write(string)
