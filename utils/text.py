import functools
import re


def remove_number_commas_on():
    """Removes commas from a formatted text number having commas as group separator."""
    return functools.partial(re.compile("(?<=\\d),(?=\\d{3})").sub, "")
