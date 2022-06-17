# pymince

[![CI](https://github.com/rmoralespp/pymince/workflows/CI/badge.svg)](https://github.com/rmoralespp/pymince/actions?query=event%3Arelease+workflow%3ACI)
[![pypi](https://img.shields.io/pypi/v/pymince.svg)](https://pypi.python.org/pypi/pymince)
[![versions](https://img.shields.io/pypi/pyversions/pymince.svg)](https://github.com/rmoralespp/pymince)
[![codecov](https://codecov.io/gh/rmoralespp/pymince/branch/main/graph/badge.svg)](https://app.codecov.io/gh/rmoralespp/pymince)


### About
pymince is a collection of useful tools that are "missing" from the Python standard library.

Process finished with exit code 0

### Installation (via pip)

```pip install pymince```

### Tests

```
(env)$ pip install -r requirements.txt   # Ignore this command if it has already been executed
(env)$ pytest tests/
(env)# pytest --cov pymince # Tests with coverge
```

### Usage
| dictionary.py | file.py | iterator.py | json.py | logging.py | retry.py | std.py | text.py |
| -------------: | -------: | -----------: | -------: | ----------: | --------: | ------: | -------: |
| [DigestGetter](#DigestGetter) | [ensure_directory](#ensure_directory) | [all_distinct](#all_distinct) | [dump_into](#dump_into) | [StructuredFormatter](#StructuredFormatter) | [retry_if_none](#retry_if_none) | [bind_json_std](#bind_json_std) | [remove_decimal_zeros](#remove_decimal_zeros) |
| [all_true_values](#all_true_values) | [is_empty_directory](#is_empty_directory) | [all_equal](#all_equal) | [load_from](#load_from) | [timed_block](#timed_block) |  |  | [remove_number_commas](#remove_number_commas) |
| [key_or_leaf_value](#key_or_leaf_value) | [match_on_zip](#match_on_zip) | [consume](#consume) |  |  |  |  | [replace](#replace) |
|  | [open_on_zip](#open_on_zip) | [grouper](#grouper) |  |  |  |  | [string2bool](#string2bool) |
|  |  | [has_only_one](#has_only_one) |  |  |  |  | [string2year](#string2year) |
|  |  | [non_empty_or_none](#non_empty_or_none) |  |  |  |  |  |
|  |  | [replacer](#replacer) |  |  |  |  |  |
|  |  | [splitter](#splitter) |  |  |  |  |  |
|  |  | [uniquer](#uniquer) |  |  |  |  |  |
|  |  | [uniques](#uniques) |  |  |  |  |  |

#### dictionary.py *Useful functions that use dictionaries*
##### DigestGetter
```
DigestGetter(include_keys=None, exclude_keys=None)

Calculate a digest of a "jsonified" python dictionary.

:param include_keys: dictionary keys to exclude
:param exclude_keys: dictionary keys to include
:rtype: str

Usage:
    from pymince.dictionary import DigestGetter

    getter = DigestGetter(include_keys=("a",))
    getter({"a": 1, "b": 1}) # --> bb6cb5c68df4652941caf652a366f2d8
    getter({"a": 1}) # --> bb6cb5c68df4652941caf652a366f2d8
```
##### all_true_values
```
all_true_values(dictionary, keys)

Check if an dictionary has all specified keys and
key-related values as True.

:param dict dictionary:
:param keys: keys sequence
:rtype: bool

Usage:
from pymince.dictionary import all_true_values

all_true_values({"a": 1, "b": 2}, ("a", "b")) # --> True
all_true_values({"a": 1, "b": 0}, ("a", "b")) # --> False
all_true_values({"a": 1, "b": 0}, ("a",)) # --> True
```
##### key_or_leaf_value
```
key_or_leaf_value(key, dictionary)

Find leaf key in dictionary.

:param str key: Key to find.
:param dict dictionary:

Usage:
    from pymince.dictionary import key_or_leaf_value

    key_or_leaf_value('a', {}) # --> 'a'
    key_or_leaf_value('a', {'a': 'b', 'b': 'c'}) # --> 'c'
    key_or_leaf_value('a', {'a': 'a'}) # --> 'a'
```
#### file.py 
##### ensure_directory
```
ensure_directory(path, cleaning=False)

Make sure the given file path is an existing directory.
If it does not exist, a new directory will be created.

:param str path:
:param bool cleaning:
    If "cleaning" is True and a directory already exists,
    this directory and the files contained in it will be deleted.

    If "cleaning" is True and a file already exists,
    this file will be deleted.
```
##### is_empty_directory
```
is_empty_directory(path)

Function to check if the given path is an empty directory.

:param str path:
:rtype: bool
```
##### match_on_zip
```
match_on_zip(zip_file, pattern)

Make an iterator that returns file names in the zip file that
match the given pattern.
Uppercase/lowercase letters are ignored.

:param zip_file: instance of ZipFile class
:param pattern: "re.Pattern" to filter filename list
:return: Iterator with the filenames found

Usage:
    import pymince.file
    pymince.file.match_on_zip(zip_file, "^file") # --> file1.log file2.txt
```
##### open_on_zip
```
open_on_zip(zip_file, filename)

Open a file that is inside a zip file.

:param zip_file: instance of ZipFile class
:param str filename:

Usage:
-------------------------------------------------
import zipfile
from pymince.file import open_on_zip

with zipfile.ZipFile(zip_filename) as zf:
    # example1
    with open_on_zip(zf, "foo1.txt") as fd1:
        foo1_string = fd1.read()
    # example2
    with open_on_zip(zf, "foo2.txt") as fd2:
        foo2_string = fd2.read()
-------------------------------------------------
```
#### iterator.py *Functions that use iterators for efficient loops*
##### all_distinct
```
all_distinct(iterable, key=None)

Check if all the elements of a key-based iterable are distinct.

:param iterable:
:param key: None or "Callable" to compare if iterable items.
:rtype: bool

Usage:
    from pymince.iterator import all_distinct

    all_distinct([1, 1]) # --> False
    all_distinct([1, 2]) # --> True
```
##### all_equal
```
all_equal(iterable, key=None)

Check if all the elements of a key-based iterable are equals.

:param iterable:
:param key: None or "Callable" to compare if iterable items.
:rtype: bool

Usage:
    from pymince.iterator import all_equal

    all_equal([1, 1]) # --> True
    all_equal([1, 2]) # --> False
```
##### consume
```
consume(iterator)

Completely consume the given iterator.

Usage:
    from pymince.iterator import consume
    it = iter([1, 2])
    consume(it)
    next(it) # --> StopIteration
```
##### grouper
```
grouper(iterable, size)

Make an iterator that returns each element being iterable
with "size" as the maximum number of elements.

:param iterable:
:param int size: maximum size of element groups.

Usage:
    from pymince.iterator import grouper

    groups = grouper([1, 2, 3, 4, 5], 2)
    list(list(g) for g in groups) # --> [[1, 2], [3, 4], [5]]
```
##### has_only_one
```
has_only_one(iterable)

Check if given iterable has only one element.

:param iterable:
:rtype: bool

Usage:
    from pymince.iterator import has_only_one

    has_only_one([1]) # --> True
    has_only_one([1, 2]) # --> False
    has_only_one([]) # --> False
```
##### non_empty_or_none
```
non_empty_or_none(iterator)

Returns an non-empty iterator or None according to given "iterator".

:param iterator:
:return: Iterator or None

Usage:
    from pymince.iterator import non_empty_or_none

    non_empty_or_none([]) # --> None
    non_empty_or_none([1,2]) # --> 1 2
```
##### replacer
```
replacer(iterable, matcher, new_value, count=-1)

Make an iterator that returns all occurrences of the old "iterable"
replaced by "new_value".

:param iterable:
:param matcher: Callable to find occurrences. It is an occurrence if the matcher returns True.
:param new_value: Any value to replace found occurrences.
:param int count:
    Maximum number of occurrences to replace.
    -1 (the default value) means replace all occurrences.

Usage:
    from pymince.iterator import replacer

    replacer([1,2,3,1,2,3], lambda n: n == 1, None) # --> None 2 3 None 2 3
    replacer([1,2,3,1,2,3], lambda n: n == 1, None, count=1) # --> None 2 3 1 2 3
```
##### splitter
```
splitter(iterable, sep, key=None, maxsplit=-1)

Split iterable into groups of iterators according
to given delimiter.

:param iterable:
:param sep: The delimiter to split the iterable.
:param key
    A function to compare the equality of each element with the given delimiter.
    If the key function is not specified or is None, the element itself is used for compare.

:param maxsplit:
    Maximum number of splits to do.
    -1 (the default value) means no limit.

:return: Generator with consecutive groups from "iterable" without the delimiter element.

Usage:
    from pymince.iterator import splitter

    data = ["a", "b", "c", "d", "b", "e"]

    undefined_split = splitter(data, "b")
    one_split = splitter(data, "b", maxsplit=1)
    list(list(s) for s in undefined_split) # --> [["a"], ["c", "d"], ["e"]]
    list(list(s) for s in one_split) # --> [["a"], ["c", "d", "b", "e"]]
```
##### uniquer
```
uniquer(iterable, key=None)

Make an iterator that returns each element from iterable only once
respecting the input order.

Usage:
    from pymince.iterator import uniquer

    uniquer([1, 2, 3, 2]) # --> 1 2 3
```
##### uniques
```
uniques(iterable, key=None)

Check if all the elements of a key-based iterable are unique.

:param iterable:
:param key: None or "Callable" to compare if iterable items.
:rtype: bool

Usage:
    from pymince.iterator import uniques

    uniques([1,2]) # --> True
    uniques([1,1]) # --> False
```
#### json.py 
##### dump_into
```
dump_into(filename, payload, indent=2)

Dump JSON to a file.

Usage:
    from pymince.json import dump_into

    dump_into("foo.json", {"key": "value"})
```
##### load_from
```
load_from(filename)

Load JSON from a file.

Usage:
    from pymince.json import load_from

    dictionary = load_from("foo.json")
```
#### logging.py 
##### StructuredFormatter
```
StructuredFormatter(fmt=None, datefmt=None, style='%', validate=True)

Implementation of JSON structured logging that works
for most handlers.

Usage in runtime
    from pymince.logging in StructuredFormatter

    # Config
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)
    formatter = StructuredFormatter('%(message)s')
    handler = logging.StreamHandler(sys.stdout)
    handler.setLevel(logging.DEBUG)
    handler.setFormatter(formatter)
    logger.addHandler(handler)

    # Usage
    logger.debug('', {"key": "value", "numb": 1, "bool": True, "nested": [1, 2, 3]})
```
##### timed_block
```
timed_block(name, logger=None)

Logger the duration of the handled context.

Usage:
    from pymince.logging import timed_block

    logging.basicConfig(level=logging.DEBUG)
    with timed_block("sleeping"):
        time.sleep(1)

    >>Output<<
    INFO:root:Generating [sleeping]
    DEBUG:root:Finished [sleeping in 1.002 ms.]
```
#### retry.py 
##### retry_if_none
```
retry_if_none(delay=0, tries=1)

Returns a retry decorator if the callback
returns None.

:param int delay: seconds delay between attempts. default: 0.
:param int tries: number of attempts. default: 1

Usage:
    @retry_if_none(delay=0, tries=1)
    def foo():
        return 1
```
#### std.py 
##### bind_json_std
```
bind_json_std(encoding='utf-8')

Decorator to call "function" passing the json read from
"stdin" in the keyword parameter "data" and dump the json that the callback returns
to "stdout".
```
#### text.py *Useful functions for working with strings.*
##### remove_decimal_zeros
```
remove_decimal_zeros(value, decimal_sep='.', min_decimals=None)

Removes non-significant decimal zeros from a formatted text number.

Usage:
    from pymince.text import remove_decimal_zeros

    remove_decimal_zeros("2.000100", ".") # --> "2.0001"
    remove_decimal_zeros("2.000000", ".") # --> "2"
    remove_decimal_zeros("2.000000", ".", min_decimals=2) # --> "2.00"
```
##### remove_number_commas
```
remove_number_commas(string)

Removes commas from a formatted text number having commas
as group separator.

:param str string:
:rtype str

Usage:
    from pymince.text import remove_number_commas
    remove_number_commas('1,234,567.8') # --> '1234567.8'
```
##### replace
```
replace(value, old_values, new_value, count=-1)

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
```
##### string2bool
```
string2bool(value, ignorecase=False)

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
```
##### string2year
```
string2year(value, gte=None, lte=None, shift=None)

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
```
### Upgrade README.md

Upgrade README.md `Usage` section according to current *pymince* code.
```
(env) python upgrade_readme_usage.py
```
