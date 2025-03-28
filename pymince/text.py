# -*- coding: utf-8 -*-

"""Useful functions for working with strings."""

import collections
import functools
import html
import random
import re
import secrets
import string
import unicodedata
import urllib.parse

import pymince.algorithm

__remove_number_commas = functools.partial(re.compile("(?<=\\d),(?=\\d{3})").sub, "")

_int_regexp_any = re.compile(r"^[-+]?[0-9]\d*$")
_int_regexp_pos = re.compile(r"^[+]?[1-9]\d*$")
_int_regexp_neg = re.compile(r"^-[1-9]\d*$")
_bin_regexp_not = re.compile(r"[^01]")
_percentage_regexp = re.compile(r"^(?:0|[1-9]\d*)(?:\.\d+)?(?:\s)?%$")
_email_address_regexp = re.compile(r"^\S+@\S+$")
_roman_regex = re.compile(r"^M{0,3}(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})$")
_re_newlines = re.compile(r"\r\n|\r")  # used in normalize_newlines
_camel2snake = re.compile(r"(?!^)([A-Z]+)")


def get_random_string(length, alphabet=string.ascii_letters):
    """Generate random string."""

    return "".join(random.choice(alphabet) for _ in range(length))


def get_random_secret(length, alphabet=string.ascii_letters):
    """
    Generate a cryptographically secure random string.
    Useful for creating temporary passwords.
    """

    return "".join(secrets.choice(alphabet) for _ in range(length))


def normalize_newlines(s):
    """Normalize CRLF and CR newlines to just LF."""

    return _re_newlines.sub("\n", s)


def remove_number_commas(s):
    """
    Removes commas from a formatted text number having commas
    as group separator.

    :param str s:
    :rtype str

    Examples:
        from pymince.text import remove_number_commas
        remove_number_commas('1,234,567.8') # --> '1234567.8'
    """

    return __remove_number_commas(s)


def replace(value, old_values, new_value, count=-1):
    """
    Replace matching values \u200b\u200bin the given string with new_value.

    :param str value:
    :param old_values: Iterable of values \u200b\u200bto replace.
    :param str new_value: Replacement value.
    :param int count:
        Maximum number of occurrences to replace.
        -1 (the default value) means replace all occurrences.
    :rtype: str

    Examples:
        from pymince.text import replace

        replace("No, woman, no cry", [","], ";") # --> "No; woman; no cry"
        replace("No, woman, no cry", [","], ";", count=1) # --> "No; woman, no cry"
    """

    for old_value in old_values:
        value = value.replace(old_value, new_value, count)
    return value


def multireplacer(replacements):
    """
    Given a replacement map, returns a function that can be reused to replace any string.

    :param Union[dict[str, str], tuple[tuple[str, str], ...] replacements:
        2-dict or 2-tuples with value to find and value to replace
    :rtype: Callable[[str], str]

     Examples:
        from pymince.text import multireplacer

        mapping = (("abc", "123"), ("def", "456"))
        replace = multireplacer(mapping)

        replace("...def...")  # --> "...456..."
        replace("...abc...")  # --> "...123..."
        replace("...abc...def...")  # --> "...123...456..."
    """

    mapper = dict(replacements)  # ensure dict
    # Place longer ones first to keep shorter substrings from matching
    # where the longer ones should take place.
    values = map(re.escape, sorted(dict(mapper), key=len, reverse=True))
    regexp = re.compile('|'.join(values))
    return functools.partial(regexp.sub, lambda match: mapper[match.group(0)])


def multireplace(text, replacements):
    """
    Given a string and a replacement map, it returns the replaced string.

    :param str text: string to execute replacements on.
    :param Union[dict[str, str], tuple[tuple[str, str], ...] replacements:
        2-dict or 2-tuples with value to find and value to replace
    :rtype: str

     Examples:
        from pymince.text import multireplace

        mapping = {",": "", "cry": "smile"}
        multireplace("No, woman, no cry", mapping) # --> "No woman no smile"

    """

    return multireplacer(replacements)(text) if replacements else text


def remove_decimal_zeros(value, decimal_sep=".", min_decimals=None):
    """
    Removes non-significant decimal zeros from a formatted text number.

    Examples:
        from pymince.text import remove_decimal_zeros

        remove_decimal_zeros("2.000100", ".") # --> "2.0001"
        remove_decimal_zeros("2.000000", ".") # --> "2"
        remove_decimal_zeros("2.000000", ".", min_decimals=2) # --> "2.00"
    """

    if not value:
        return ""

    int_part, _, dec_part = value.partition(decimal_sep)
    int_part = int_part or "0"  # ensure ('.1' => '0.1')
    # remove decimal zeros to the right.
    dec_part = dec_part.rstrip("0")
    dec_part_size = len(dec_part)
    # If the integer part is not 0, it is checked if it is necessary
    # to add decimals to decimal part based on "min_decimals" param
    if int_part != "0" and min_decimals and dec_part_size < min_decimals:
        dec_diff = "0" * (min_decimals - dec_part_size)
        dec_part = f"{dec_part}{dec_diff}"

    return f"{int_part}{decimal_sep}{dec_part}" if dec_part else int_part


def slugify(value, allow_unicode=False):
    """
    Convert to ASCII if 'allow_unicode' is False. Convert spaces or repeated
    dashes to single dashes. Remove characters that aren't alphanumerics,
    underscores, or hyphens. Convert to lowercase. Also strip leading and
    trailing whitespace, dashes, and underscores.

    https://github.com/django/django/blob/main/django/utils/text.py
    """

    value = str(value)
    if allow_unicode:
        value = unicodedata.normalize("NFKC", value)
    else:
        value = unicodedata.normalize("NFKD", value).encode("ascii", "ignore").decode("ascii")
    value = re.sub(r"[^\w\s-]", "", value.lower())
    return re.sub(r"[-\s]+", "-", value).strip("-_")


def camel2snake(camel_str):
    """Convert CamelCase to snake_case."""

    return _camel2snake.sub(r"_\1", camel_str).lower()


def is_url(text, schemes=None, hostnames=None):
    """
    Check if the string is a URL according to the
    given schemes and host-names.

    :param str text:
    :param Optional[Container[str]] schemes: ("http", "https")
    :param Optional[Container[str]] hostnames: ("www.python.org", "github.com", "localhost")
    :rtype: bool

    Examples:
        from pymince.text import is_url

        # True
        is_url("https://github.com/")
        is_url("https://github.com/", hostnames=("github.com",))
        is_url("https://github.com/", hostnames=("github.com",), schemes=("https",))

        # False
        is_url("https://github.com/", schemes=("http",))
        is_url("https://github.com/", hostnames=("www.python.org", "localhost"))
    """

    res = urllib.parse.urlparse(text)
    if not res.scheme or (schemes and res.scheme not in schemes):
        return False
    if not res.netloc or (hostnames and res.hostname not in hostnames):
        return False
    try:
        _ = res.port
    except ValueError:
        return False
    else:
        return True


def is_binary(text):
    """Check if the string is binary or not."""

    return not next(_bin_regexp_not.finditer(text), None)


def is_int(text):
    """
    Check if the string is the representation of
    an integer number.

    True: "10", "+10", "-10", "0"
    """

    return _int_regexp_any.fullmatch(text) is not None


def is_positive_int(text):
    """
    Check if the string is the representation of
    positive integer number.

    True: "10", "+10"
    """

    return _int_regexp_pos.fullmatch(text) is not None


def is_negative_int(text):
    """
    Check if the string is the representation of
    negative integer number.

    True: "-10"
    """

    return _int_regexp_neg.fullmatch(text) is not None


def is_payment_card(text):
    """
    Check if the string is a valid payment
    card number.

    https://en.wikipedia.org/wiki/Payment_card_number#Issuer_identification_number_(IIN)
    """

    numb = text.replace(" ", "")
    size = len(numb)
    if 12 <= size <= 19 and pymince.algorithm.luhn(numb):
        if numb[0] == "4":  # Visa
            isvalid = size in {13, 16, 19}
        elif 51 <= int(numb[:2]) <= 55:  # Mastercard
            isvalid = size == 16
        elif numb[:2] in {"34", "37"}:  # American Express
            isvalid = size == 15
        else:
            isvalid = True
        return isvalid
    else:
        return False


def is_email_address(text):
    """
    Check if the string is an email address.

    This solution does a very simple check. It only validates that the string contains an at sign (@)
    that is preceded and followed by one or more non whitespace characters.
    """
    return _email_address_regexp.fullmatch(text) is not None


def is_percentage(text):
    """
    Check if the string is a valid percentage

    True: "100%", "100 %", "100&nbsp;%", 100.0 %",
    """

    unescaped = html.unescape(text)  # 100&nbsp;% => 100 %
    return _percentage_regexp.fullmatch(unescaped) is not None


def is_palindrome(text):
    """
    Check if the string is palindrome or not.
    A string is said to be palindrome if the reverse of the string is the same as string
    """

    return text == text[::-1]


def is_roman(text):
    """Check if the string is a valid roman numeral."""

    return _roman_regex.fullmatch(text) is not None


def are_anagram(text1, text2):
    """
    Check if two strings are anagram.

    Examples:
        from pymince.text import are_anagram

        are_anagram("listen", "silent")      # --> True
        are_anagram("they see", "the eyes")  # --> True
    """

    return collections.Counter(text1) == collections.Counter(text2)
