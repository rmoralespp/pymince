import functools
import re

remove_number_commas = functools.partial(re.compile("(?<=\\d),(?=\\d{3})").sub, "")
remove_number_commas.__doc__ = """Removes commas from a formatted text number having commas as group separator."""
