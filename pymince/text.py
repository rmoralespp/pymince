"""
Useful functions for working with strings.
"""
import contextlib
import datetime
import functools
import re

__remove_number_commas = functools.partial(re.compile("(?<=\\d),(?=\\d{3})").sub, "")


def remove_number_commas(string):
    """
    Removes commas from a formatted text number having commas
    as group separator.

    :param str string:
    :rtype str

    Usage:
        from pymince.text import remove_number_commas
        remove_number_commas('1,234,567.8') # --> '1234567.8'
    """

    return __remove_number_commas(string)


def replace(value, old_values, new_value, count=-1):
    """
    Replace matching values ​​in the given string with new_value.

    :param str value:
    :param old_values: iterable of values ​​to replace.
    :param str new_value: replacement value.
    :param int count:
        Maximum number of occurrences to replace.
        -1 (the default value) means replace all occurrences.
    :rtype: str

    Usage:
        from pymince.text import replace

        replace("No, woman, no cry", [","], ";") # --> "No; woman; no cry"
        replace("No, woman, no cry", [","], ";", count=1) # --> "No; woman, no cry"
    """

    for old_value in old_values:
        value = value.replace(old_value, new_value, count)
    return value


def remove_decimal_zeros(value, decimal_sep='.', min_decimals=None):
    """
    Removes non-significant decimal zeros from a formatted text number.

    Usage:
        from pymince.text import remove_decimal_zeros

        remove_decimal_zeros("2.000100", ".") # --> "2.0001"
        remove_decimal_zeros("2.000000", ".") # --> "2"
        remove_decimal_zeros("2.000000", ".", min_decimals=2) # --> "2.00"
    """

    if not value:
        return ''

    int_part, _, dec_part = value.partition(decimal_sep)
    int_part = int_part or '0'  # ensure ('.1' => '0.1')
    # remove decimal zeros to the right.
    dec_part = dec_part.rstrip('0')
    dec_part_size = len(dec_part)
    # If the integer part is not 0, it is checked if it is necessary
    # to add decimals to decimal part based on "min_decimals" param
    if int_part != '0' and min_decimals and dec_part_size < min_decimals:
        dec_diff = '0' * (min_decimals - dec_part_size)
        dec_part = f'{dec_part}{dec_diff}'

    return f'{int_part}{decimal_sep}{dec_part}' if dec_part else int_part


def string2bool(value, ignorecase=False):
    """
    Function to convert a string representation of
    truth to True or False.

    :param str value: value to convert.
    :param bool ignorecase: Uppercase/lowercase letters of given "value" are ignored.

    :raise: "ValueError" if "value" is anything else.
    :rtype: bool

    Usage:
        from pymince.text import string2bool

        string2bool("true") # --> True
        string2bool("false") # --> False

        string2bool("TRUE") # --> ValueError
        string2bool("TRUE", ignorecase=True) # --> True

        string2bool("FALSE") # --> ValueError
        string2bool("FALSE", ignorecase=True) # --> False
    """

    checking = value.lower() if ignorecase else value
    if checking == 'true':
        return True
    elif checking == 'false':
        return False
    else:
        raise ValueError


def string2year(value, gte=None, lte=None, shift=None):
    """
    Function to convert a string year representation to integer year.

    :param str value: Value to convert.
    :param Optional[int] gte: if it is specified is required that: year >= gte
    :param Optional[int] lte: if it is specified is required that: year <= lte
    :param Optional[int] shift: use a two-digit year on shift

    :raise: "ValueError" if "value" cannot be converted.
    :rtype: int

    Usage:
        from pymince.text import string2year

        string2year("53", shift=None) # --> 2053
        string2year("53", shift=1953) # --> 1953
        string2year("52", shift=1953) # --> 2052
        string2year("54", shift=1953) # --> 1954

        string2year("1954") # --> 1954

        string2year("123") # --> ValueError
        string2year("1955", gte=1956) # --> ValueError
        string2year("1955", lte=1954) # --> ValueError
    """

    year = None
    for rep in ('%Y', '%y'):
        with contextlib.suppress(ValueError, TypeError):
            year = datetime.datetime.strptime(value, rep).year
            if shift and rep == '%y':
                # Use shift for year of two-digit format
                year = (year - shift) % 100 + shift
            if (gte and not year >= gte) or (lte and not year <= lte):
                year = None
            break

    if year:
        return year
    else:
        raise ValueError
