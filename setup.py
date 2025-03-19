# -*- coding: utf-8 -*-
from setuptools import setup

from pymince import __version__, __title__


def read(filename):
    with open(filename, encoding="utf-8") as f:
        return f.read()


def get_long_description():
    blocks = (
        read("README.md"),
        # Fixme read("CHANGELOG.md"),
    )
    return "\n".join(blocks)


setup(
    name=__title__,
    version=__version__,
    description="Python shredded utilities",
    long_description=get_long_description(),
    long_description_content_type="text/markdown",
    classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Programming Language :: Python :: 3.13",
        "Intended Audience :: Developers",
        "Intended Audience :: Information Technology",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Internet",
        "Topic :: Utilities",
    ],
    keywords="",
    author="rmoralespp",
    author_email="rmoralespp@gmail.com",
    url="https://github.com/rmoralespp/pymince",
    license="MIT",
    packages=["pymince"],
    include_package_data=True,
    zip_safe=False,  # https://mypy.readthedocs.io/en/latest/installed_packages.html
    # install_requires=read('requirements.txt'),
    python_requires=">=3.8",
)
