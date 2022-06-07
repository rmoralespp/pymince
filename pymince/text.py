import functools
import re

remove_number_commas = functools.partial(re.compile("(?<=\\d),(?=\\d{3})").sub, "")
remove_number_commas.__doc__ = """Removes commas from a formatted text number having commas as group separator."""


def remove_decimal_zeros(value, decimal_sep='.', min_decimals=None):
    """
    Removes non-significant decimal zeros from a formatted text number.

    Usage:
    >> remove_decimal_zeros("2.000100", ".") => "2.0001"
    >> remove_decimal_zeros("2.000000", ".") => "2"
    >> remove_decimal_zeros("2.000000", ".", min_decimals=2) => "2.00"
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
