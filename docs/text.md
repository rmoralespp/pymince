# Text
Useful functions for working with strings.

**are_anagram**
```
are_anagram(text1, text2)

Check if two strings are anagram.

Examples:
    from pymince.text import are_anagram

    are_anagram("listen", "silent")      # --> True
    are_anagram("they see", "the eyes")  # --> True
```
**camel2snake**
```
camel2snake(camel_str)

Convert CamelCase to snake_case.
```
**get_random_secret**
```
get_random_secret(length, alphabet='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')

Generate a cryptographically secure random string.
Useful for creating temporary passwords.
```
**get_random_string**
```
get_random_string(length, alphabet='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')

Generate random string.
```
**is_binary**
```
is_binary(text)

Check if the string is binary or not.
```
**is_email_address**
```
is_email_address(text)

Check if the string is an email address.

This solution does a very simple check. It only validates that the string contains an at sign (@)
that is preceded and followed by one or more non whitespace characters.
```
**is_int**
```
is_int(text)

Check if the string is the representation of
an integer number.

True: "10", "+10", "-10", "0"
```
**is_negative_int**
```
is_negative_int(text)

Check if the string is the representation of
negative integer number.

True: "-10"
```
**is_palindrome**
```
is_palindrome(text)

Check if the string is palindrome or not.
A string is said to be palindrome if the reverse of the string is the same as string
```
**is_payment_card**
```
is_payment_card(text)

Check if the string is a valid payment
card number.

https://en.wikipedia.org/wiki/Payment_card_number#Issuer_identification_number_(IIN)
```
**is_percentage**
```
is_percentage(text)

Check if the string is a valid percentage

True: "100%", "100 %", "100&nbsp;%", 100.0 %",
```
**is_positive_int**
```
is_positive_int(text)

Check if the string is the representation of
positive integer number.

True: "10", "+10"
```
**is_roman**
```
is_roman(text)

Check if the string is a valid roman numeral.
```
**is_url**
```
is_url(text, schemes=None, hostnames=None)

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
```
**multireplace**
```
multireplace(text, replacements)

Given a string and a replacement map, it returns the replaced string.

:param str text: string to execute replacements on.
:param Union[dict[str, str], tuple[tuple[str, str], ...] replacements:
    2-dict or 2-tuples with value to find and value to replace
:rtype: str

 Examples:
    from pymince.text import multireplace

    mapping = {",": "", "cry": "smile"}
    multireplace("No, woman, no cry", mapping) # --> "No woman no smile"
```
**multireplacer**
```
multireplacer(replacements)

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
```
**normalize_newlines**
```
normalize_newlines(s)

Normalize CRLF and CR newlines to just LF.
```
**remove_decimal_zeros**
```
remove_decimal_zeros(value, decimal_sep='.', min_decimals=None)

Removes non-significant decimal zeros from a formatted text number.

Examples:
    from pymince.text import remove_decimal_zeros

    remove_decimal_zeros("2.000100", ".") # --> "2.0001"
    remove_decimal_zeros("2.000000", ".") # --> "2"
    remove_decimal_zeros("2.000000", ".", min_decimals=2) # --> "2.00"
```
**remove_number_commas**
```
remove_number_commas(s)

Removes commas from a formatted text number having commas
as group separator.

:param str s:
:rtype str

Examples:
    from pymince.text import remove_number_commas
    remove_number_commas('1,234,567.8') # --> '1234567.8'
```
**replace**
```
replace(value, old_values, new_value, count=-1)

Replace matching values ​​in the given string with new_value.

:param str value:
:param old_values: Iterable of values ​​to replace.
:param str new_value: Replacement value.
:param int count:
    Maximum number of occurrences to replace.
    -1 (the default value) means replace all occurrences.
:rtype: str

Examples:
    from pymince.text import replace

    replace("No, woman, no cry", [","], ";") # --> "No; woman; no cry"
    replace("No, woman, no cry", [","], ";", count=1) # --> "No; woman, no cry"
```
**slugify**
```
slugify(value, allow_unicode=False)

Convert to ASCII if 'allow_unicode' is False. Convert spaces or repeated
dashes to single dashes. Remove characters that aren't alphanumerics,
underscores, or hyphens. Convert to lowercase. Also strip leading and
trailing whitespace, dashes, and underscores.

https://github.com/django/django/blob/main/django/utils/text.py
```