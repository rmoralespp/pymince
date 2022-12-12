"""
Useful functions for working with strings.
"""
import functools
import re
import urllib.parse

import pymince.algorithm

__remove_number_commas = functools.partial(re.compile("(?<=\\d),(?=\\d{3})").sub, "")

_int_regexp_any = re.compile(r"^[-+]?[1-9]\d*\.?[0]*$")
_int_regexp_pos = re.compile(r"^[+]?[1-9]\d*\.?[0]*$")
_int_regexp_neg = re.compile(r"^-[1-9]\d*\.?[0]*$")
_bin_regexp_not = re.compile('[^01]')


class fullstr(str):
    """
    Custom string inheriting from "str" which adds
    the following methods:

    - is_url(self, schemes=None, hostnames=None)
    - is_int(self)
    - is_positive_int(self)
    - is_negative_int(self)
    - is_payment_card(self)
    - is_binary(self)
    - is_email_address(self) # TODO
    - is_percent(self)  # TODO

    Examples:
        from pymince.text import fullstr

        fullstr("6011 0000 0000 0012").is_payment_card() # True
    """

    def is_url(self, schemes=None, hostnames=None):
        """
        Check if the string is a URL according to the
        given schemes and host-names.

        :param Optional[Container[str]] schemes: ("http", "https")
        :param Optional[Container[str]] hostnames: ("www.python.org", "github.com", "localhost")
        :rtype: bool

        Examples:
            from pymince.text import fullstr

            # True
            fullstr("https://github.com/").is_url()
            fullstr("https://github.com/").is_url(hostnames=("github.com",))
            fullstr("https://github.com/").is_url(schemes=("https",), hostnames=("github.com",))

            # False
            fullstr("https://github.com/").is_url(schemes=("http",))
            fullstr("https://github.com/").is_url(hostnames=("www.python.org", "localhost"))
        """

        res = urllib.parse.urlparse(self)
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

    def is_binary(self):
        """Check if the string is binary or not."""
        return not next(_bin_regexp_not.finditer(self), None)

    def is_int(self):
        """
        Check if the string is the representation of
        a integer number.

        True:
         "10",   "10.",   "10.0",
        "+10",  "+10.",  "+10.0",
        "-10",  "-10.",  "-10.0"
        """
        return bool(_int_regexp_any.fullmatch(self))

    def is_positive_int(self):
        """
        Check if the string is the representation of
        positive integer number.

        True:
         "10",   "10.",   "10.0",
        "+10",  "+10.",  "+10.0",
        """
        return bool(_int_regexp_pos.fullmatch(self))

    def is_negative_int(self):
        """
        Check if the string is the representation of
        negative integer number.

        True:
        "-10",  "-10.",  "-10.0"
        """

        return bool(_int_regexp_neg.fullmatch(self))

    def is_payment_card(self):
        """
        Check if the string is a valid payment
        card number.

        https://en.wikipedia.org/wiki/Payment_card_number#Issuer_identification_number_(IIN)
        """

        numb = self.replace(" ", "")
        size = len(numb)
        if 12 <= size <= 19 and pymince.algorithm.luhn(numb):
            if numb[0] == '4':  # Visa
                isvalid = size in {13, 16, 19}
            elif 51 <= int(numb[:2]) <= 55:  # Mastercard
                isvalid = size == 16
            elif numb[:2] in {'34', '37'}:  # American Express
                isvalid = size == 15
            else:
                isvalid = True
            return isvalid
        else:
            return False

    def is_email_address(self):
        raise NotImplementedError

    def is_percent(self):
        raise NotImplementedError


def remove_number_commas(string):
    """
    Removes commas from a formatted text number having commas
    as group separator.

    :param str string:
    :rtype str

    Examples:
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

    Examples:
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

    Examples:
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
