# pymince

[![CI](https://github.com/rmoralespp/pymince/workflows/CI/badge.svg)](https://github.com/rmoralespp/pymince/actions?query=event%3Arelease+workflow%3ACI)
[![pypi](https://img.shields.io/pypi/v/pymince.svg)](https://pypi.python.org/pypi/pymince)
[![versions](https://img.shields.io/pypi/pyversions/pymince.svg)](https://github.com/rmoralespp/pymince)
[![codecov](https://codecov.io/gh/rmoralespp/pymince/branch/main/graph/badge.svg)](https://app.codecov.io/gh/rmoralespp/pymince)
[![license](https://img.shields.io/github/license/rmoralespp/pymince.svg)](https://github.com/rmoralespp/pymince/blob/main/LICENSE)
[![Downloads](https://pepy.tech/badge/pymince)](https://pepy.tech/project/pymince)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Linter: ruff](https://img.shields.io/badge/linter-_ruff-orange)](https://github.com/charliermarsh/ruff)
[![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit)](https://github.com/pre-commit/pre-commit)

### About
pymince is a collection of useful tools that are "missing" from the Python standard library.


### Installation (via pip)

```pip install pymince```

### Tests

```
(env)$ pip install -r requirements.txt   # Ignore this command if it has already been executed
(env)$ pytest tests/
(env)$ pytest --cov pymince # Tests with coverge
```

### Usage
| PyModules  | Tools  |
| :--------  | :----- |
| **algorithm.py** |[*fibonacci*](#fibonacci), [*luhn*](#luhn), [*sieve_of_eratosthenes*](#sieve_of_eratosthenes)|
| **boolean.py** |[*string2bool*](#string2bool)|
| **dates.py** |[*IsoWeekDay*](#IsoWeekDay), [*WeekDay*](#WeekDay), [*irange*](#irange), [*string2year*](#string2year)|
| **dictionary.py** |[*DigestGetter*](#DigestGetter), [*all_true_values*](#all_true_values), [*find_leaf_value*](#find_leaf_value), [*from_objects*](#from_objects), [*frozendict*](#frozendict), [*tree*](#tree)|
| **file.py** |[*decompress*](#decompress), [*ensure_directory*](#ensure_directory), [*get_valid_filename*](#get_valid_filename), [*is_empty_directory*](#is_empty_directory), [*match_from_zip*](#match_from_zip), [*replace_extension*](#replace_extension)|
| **functional.py** |[*caller*](#caller), [*classproperty*](#classproperty), [*identity*](#identity), [*once*](#once), [*pipe*](#pipe), [*retry_if_errors*](#retry_if_errors), [*retry_if_none*](#retry_if_none), [*set_attributes*](#set_attributes), [*suppress*](#suppress)|
| **iterator.py** |[*all_distinct*](#all_distinct), [*all_equal*](#all_equal), [*all_equals*](#all_equals), [*all_identical*](#all_identical), [*centroid*](#centroid), [*consume*](#consume), [*grouper*](#grouper), [*ibool*](#ibool), [*in_all*](#in_all), [*in_any*](#in_any), [*ipush*](#ipush), [*mul*](#mul), [*only_one*](#only_one), [*pad_end*](#pad_end), [*pad_start*](#pad_start), [*partition*](#partition), [*replacer*](#replacer), [*splitter*](#splitter), [*sub*](#sub), [*truediv*](#truediv), [*uniquer*](#uniquer), [*uniques*](#uniques)|
| **json.py** |[*JSONEncoder*](#JSONEncoder), [*dump_from_csv*](#dump_from_csv), [*dump_into*](#dump_into), [*dump_into_zip*](#dump_into_zip), [*idump_fork*](#idump_fork), [*idump_into*](#idump_into), [*idump_lines*](#idump_lines), [*load_from*](#load_from), [*load_from_zip*](#load_from_zip)|
| **jsonlines.py** |[*dump*](#dump), [*dump_fork*](#dump_fork), [*dump_into*](#dump_into), [*dumper*](#dumper), [*dumps*](#dumps), [*load*](#load), [*load_from*](#load_from)|
| **logging.py** |[*StructuredFormatter*](#StructuredFormatter), [*timed_block*](#timed_block)|
| **std.py** |[*bind_json_std*](#bind_json_std)|
| **text.py** |[*are_anagram*](#are_anagram), [*fullstr*](#fullstr), [*get_random_secret*](#get_random_secret), [*get_random_string*](#get_random_string), [*is_binary*](#is_binary), [*is_email_address*](#is_email_address), [*is_int*](#is_int), [*is_negative_int*](#is_negative_int), [*is_palindrome*](#is_palindrome), [*is_payment_card*](#is_payment_card), [*is_percentage*](#is_percentage), [*is_positive_int*](#is_positive_int), [*is_roman*](#is_roman), [*is_url*](#is_url), [*multireplace*](#multireplace), [*multireplacer*](#multireplacer), [*normalize_newlines*](#normalize_newlines), [*remove_decimal_zeros*](#remove_decimal_zeros), [*remove_number_commas*](#remove_number_commas), [*replace*](#replace)|
| **warnings.py** |[*deprecated*](#deprecated)|
| **xml.py** |[*iterparse*](#iterparse)|

#### algorithm.py

##### fibonacci
```
fibonacci(n=None)

Returns a generator with fibonacci series up to n.
Runs indefinitely if n is specified as None.

:param Optional[int] n: Must be None or number.
:rtype: Generator[int]
```
##### luhn
```
luhn(value: str) -> bool

The Luhn algorithm or Luhn formula, also known as the "modulus 10" or "mod 10" algorithm,
named after its creator, IBM scientist Hans Peter Luhn,
is a simple checksum formula used to validate a variety of
identification numbers, such as credit card numbers, IMEI numbers, National Provider Identifier numbers

Based on: https://en.wikipedia.org/wiki/Luhn_algorithm
```
##### sieve_of_eratosthenes
```
sieve_of_eratosthenes(n)

Primes less than n.
Based on: https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes

:param int n: n an integer n > 1
:rtype: Generator[int]. All prime numbers from 2 through n.

Examples:
    from pymince.algorithm import sieve_of_eratosthenes as primes
    primes(30) # --> 2, 3, 5, 7, 11, 13, 17, 19, 23, 29
```
#### boolean.py

##### string2bool
```
string2bool(value, ignorecase=False)

Function to convert a string representation of
truth to True or False.

:param str value: value to convert.
:param bool ignorecase: Uppercase/lowercase letters of given "value" are ignored.

:raise: "ValueError" if "value" is anything else.
:rtype: bool

Examples:
    from pymince.boolean import string2bool

    string2bool("true") # --> True
    string2bool("false") # --> False

    string2bool("TRUE") # --> ValueError
    string2bool("TRUE", ignorecase=True) # --> True

    string2bool("FALSE") # --> ValueError
    string2bool("FALSE", ignorecase=True) # --> False
```
#### dates.py

##### IsoWeekDay
```
IsoWeekDay(value, names=None, *, module=None, qualname=None, type=None, start=1)

Python Enum containing Days of the Week, according to ISO,
where Monday == 1 ... Sunday == 7.

Provides a 'of' method can be used to verbalize a datetime.datetime.isoweekday
return value.

Example:
     from pymince.dates import IsoWeekDay

    friday = datetime.datetime(2023, 2, 17)
    IsoWeekDay.of(friday)  #  pymince.dates.IsoWeekDay.FRIDAY
```
##### WeekDay
```
WeekDay(value, names=None, *, module=None, qualname=None, type=None, start=1)

Python Enum containing Days of the Week,
where Monday == 0 ... Sunday == 6.

Provides a 'of' method can be used to verbalize a datetime.datetime.weekday
return value.

Example:
    from pymince.dates import WeekDay

    friday = datetime.datetime(2023, 2, 17)
    WeekDay.of(friday)  #  pymince.dates.WeekDay.FRIDAY
```
##### irange
```
irange(start_date, stop_date=None, time_step=None)

Returns a generator that produces a sequence of datetime's from "start_date" (inclusive)
to "stop_date" (exclusive) by "time_step".

:param datetime.datetime start_date: Inclusive.
:param datetime.datetime stop_date: Exclusive. `utcnow` is used by default.
:param datetime.delta time_step: one-day `timedelta` is used by default.

 Examples:
    import datetime

    from pymince.dates import irange

    ini = datetime.datetime.fromisoformat("2022-10-31")
    end = datetime.datetime.fromisoformat("2022-11-02")
    day = datetime.timedelta(days=1)

    it = irange(ini, stop_date=end, time_step=day)

    next(it) # --> datetime.datetime(2022, 10, 31, 0, 0)
    next(it) # --> datetime.datetime(2022, 11, 1, 0, 0)
    next(it) # --> raise StopIteration
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

Examples:
    from pymince.dates import string2year

    string2year("53", shift=None) # --> 2053
    string2year("53", shift=1953) # --> 1953
    string2year("52", shift=1953) # --> 2052
    string2year("54", shift=1953) # --> 1954

    string2year("1954") # --> 1954

    string2year("123") # --> ValueError
    string2year("1955", gte=1956) # --> ValueError
    string2year("1955", lte=1954) # --> ValueError
```
#### dictionary.py
Useful functions that use dictionaries.
##### DigestGetter
```
DigestGetter(include_keys=None, exclude_keys=None)

Calculate a digest of a "jsonified" python dictionary.

:param include_keys: dictionary keys to exclude
:param exclude_keys: dictionary keys to include
:rtype: str

Examples:
    from pymince.dictionary import DigestGetter

    getter = DigestGetter(include_keys=("a",))
    getter({"a": 1, "b": 1}) # --> bb6cb5c68df4652941caf652a366f2d8
    getter({"a": 1}) # --> bb6cb5c68df4652941caf652a366f2d8
```
##### all_true_values
```
all_true_values(dictionary, keys)

Check if a dictionary has all the specified keys and if all its
evaluated key-related values are True.

:param dict dictionary:
:param keys: keys sequence
:rtype: bool

Examples:
from pymince.dictionary import all_true_values

all_true_values({"a": 1, "b": 2}, ("a", "b")) # --> True
all_true_values({"a": 1, "b": 0}, ("a", "b")) # --> False
all_true_values({"a": 1, "b": 0}, ("a",)) # --> True
```
##### find_leaf_value
```
find_leaf_value(key, dictionary)

Find leaf value in mapping.

:param Any key: key to find
:param dict dictionary:

Examples:
    from pymince.dictionary import find_leaf_value

    find_leaf_value('a', {}) # --> 'a'
    find_leaf_value('a', {'a': 'b', 'b': 'c'}) # --> 'c'
    find_leaf_value('a', {'a': 'a'}) # --> 'a'
```
##### from_objects
```
from_objects(iterable, key_getter, value_getter)

Create a new dictionary with elements generated from
the "key_getter" and "value_getter" callbacks applied to each element of the iterable.

:param Iterable[any] iterable:
:param Callable key_getter:
    Dictionary keys getter.
    It is called with each element of "iterable" passing it as an argument.
:param Callable value_getter:
    Dictionary values getter.
    It is called with each element of "iterable" passing it as an argument.

:raise: ValueError if any generated key is duplicate.
:rtype: dict

Examples:
    from pymince.dictionary import from_objects

    keygetter = operator.itemgetter(0)
    valgetter = operator.itemgetter(1, 2)

    values = iter([(1, "a", "b"), (2, "a", "b")])
    from_objects(values, keygetter, valgetter) # --> {1: ('a', 'b'), 2: ('a', 'b')}
```
##### frozendict
```
frozendict(*args, **kwargs)

Returns a "MappingProxyType" from a dictionary built according to given parameters.
Add immutability only on a first level.

Examples:
    from pymince.dictionary import frozendict

    my_dict = frozendict(a=1, b=2)
    my_dict["a"] # --> 1
    list(my_dict.items())  # --> [("a", 1), ("b", 2)]
    my_dict["c"] = 3  # --> TypeError
```
##### tree
```
tree()

Returns a dict whose defaults are dicts.
As suggested here: https://gist.github.com/2012250

Examples:
    import json

    from pymince.dictionary import tree

    users = tree()
    users['user1']['username'] = 'foo'
    users['user2']['username'] = 'bar'

    print(json.dumps(users))  # {"user1": {"username": "foo"}, "user2": {"username": "bar"}}
```
#### file.py

##### decompress
```
decompress(src_path, dst_path, size=65536)

Decompress given file in blocks using gzip.

:param str src_path: source file path
:param str dst_path: destination file(unzipped) path
:param int size: Read up to size bytes from src_path for each block.
:return: dst_path

 Examples:
    from pymince.file import decompress

    decompress("/foo/src.txt.gz", "/baz/dst.txt")  # --> "/baz/dst.txt"
```
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
##### get_valid_filename
```
get_valid_filename(s)

Returns a valid filename for the given string.

- Remove leading/trailing spaces
- Change spaces to underscores
- Remove anything that is not an alphanumeric, dash, underscore, or dot
```
##### is_empty_directory
```
is_empty_directory(path)

Check if the given path is an empty directory.
```
##### match_from_zip
```
match_from_zip(zip_file, pattern)

Make an iterator that returns file names in the zip file that
match the given pattern.
Uppercase/lowercase letters are ignored.

:param zip_file: ZipFile object or zip path.
:param pattern: "re.Pattern" to filter filename list
:return: Iterator with the filenames found

Examples:
    import pymince.file
    pymince.file.match_from_zip("archive.zip", "^file") # --> file1.log file2.txt
    pymince.file.match_from_zip(zipfile.ZipFile("archive.zip"), "^file") # --> file1.log file2.txt
```
##### replace_extension
```
replace_extension(filename, old_ext=None, new_ext=None)

Replace filename "old_ext" with "new_ext".

:param str filename:
:param Optional[str] old_ext:
:param Optional[str] new_ext:

Examples:
    from pymince.file import replace_extension

    # remove extensions
    replace_extension("/home/user/file.old") # --> "/home/user/file"
    replace_extension("/home/user/file.old", old_ext=".old") # --> "/home/user/file"
    replace_extension("/home/user/file.old", old_ext=".new") # --> "/home/user/file.old"

    # replace extensions
    replace_extension("/home/user/file.old", new_ext=".new") # --> "/home/user/file.new"
    replace_extension("/home/user/file.old", old_ext=".old", new_ext=".new") # --> "/home/user/file.new"
    replace_extension("/home/user/file.old", old_ext=".new", new_ext=".new") # --> "/home/user/file.old"
```
#### functional.py

##### caller
```
caller(*args, **kwargs)

Return a callable that calls with given params.

Examples:
    import pymince.functional

    caller = pymince.functional.caller(range(5))
    caller(len)   #  5
    caller(list)  # [0, 1, 2, 3, 4]
```
##### classproperty
```
classproperty(method=None)

Decorator that converts a method with a single cls argument into a property
that can be accessed directly from the class.

Examples:
    from pymince.functional import classproperty

    class MyClass:
        __foo = "var"

        @classproperty
        def foo(cls):
            return cls.__foo
```
##### identity
```
identity(x)

Takes a single argument and returns it unchanged.
Identity function, as defined in https://en.wikipedia.org/wiki/Identity_function.
```
##### once
```
once(fn)

Decorator to execute a function only once.

Examples:
    from pymince.functional import once

    @once
    def inc_once():
        global n
        n += 1
        return 'anything'

    n = 0
    inc_once()  #  --> 'anything'
    inc_once()  #  --> 'anything'
    inc_once()  #  --> 'anything'
    print(n)    #  --> 1
```
##### pipe
```
pipe(*fns)

Compose functions from left to right.

:param fns: Functions to compose.
:rtype: Callable[[Any], Any]

Examples:
    from pymince.functional import pipe

    addtwo = lambda n: n + 2
    double = lambda n: n * 2
    square = lambda n: n * n

    fn = pipe(addtwo, double, square)
    fn(1) # --> 36
```
##### retry_if_errors
```
retry_if_errors(*exceptions, delay=0, tries=1)

Decorator that retries to call the wrapped function
if any of given exceptions are thrown.

:param exceptions: Lists of exceptions that trigger a retry attempt.
:param int delay: seconds delay between attempts. default: 0.
:param int tries: number of attempts. default: 1

Examples:
@retry_if_errors(ValueError, TypeError, delay=0, tries=1)
def foo():
    return 1
```
##### retry_if_none
```
retry_if_none(delay=0, tries=1)

Decorator that retries to call the wrapped function
if it returns None.

:param int delay: seconds delay between attempts. default: 0.
:param int tries: number of attempts. default: 1

Examples:
    @retry_if_none(delay=0, tries=1)
    def foo():
        return 1
```
##### set_attributes
```
set_attributes(**kwargs)

Decorator to set attributes on functions and classes.

Examples:
    from pymince.functional import set_attributes

    @set_attributes(short_description="dummy function")
    def foo():
        pass

    print(foo.short_description)  # "dummy function"

Based on: https://github.com/wolph/python-utils/ (set_attributes)
```
##### suppress
```
suppress(*exceptions, default=None)

Decorator to suppress the specified exceptions and return the
default value instead.

Examples:
    from pymince.functional import suppress

    @suppress(FileNotFoundError, default=False)
    def remove(somefile):
         os.remove(somefile)

    remove("no_found.txt")  # False
```
#### iterator.py
Functions that use iterators for efficient loops.
##### all_distinct
```
all_distinct(iterable, key=None)

Check if all the elements of a key-based iterable are distinct.

:param iterable:
:param key: None or "Callable" to compare if iterable items.
:rtype: bool

Examples:
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

Examples:
    from pymince.iterator import all_equal

    all_equal([1, 1]) # --> True
    all_equal([1, 2]) # --> False
```
##### all_equals
```
all_equals(*iterables, key=None)

Check if the iterables are equal.
If the "iterables" are empty, it returns True.

:param iterables:
:param key: None or "Callable" to compare if iterable items.
:rtype: bool

Examples:
    from pymince.iterator import all_equals

    all_equals() # --> True
    all_equals(range(1, 4), (1, 2, 3), {1, 2, 3}) # --> True
    all_equals((1, 2), (1, 2, 3)) # --> False
```
##### all_identical
```
all_identical(left, right)

Check that the items of `left` are the same objects
as those in `right`.

:param Iterable[Any] left:
:param Iterable[Any] right:
:rtype: bool

Examples:
    from pymince.iterator import all_identical

    a, b = object(), object()
    all_identical([a, b, a], [a, b, a]) # --> True
    all_identical([a, b, [a]], [a, b, [a]])  # --> False *new list object, while "equal" is not "identical"*
```
##### centroid
```
centroid(coordinates)

Calculate the centroid of a set of n-dimensional coordinates.
In Cartesian coordinates, the centroid is
just the mean of the components.

:param Iterable[Iterable[int]] coordinates: Iterable of n-dimensional coordinates.
:rtype: Generator[int]

 Examples:
    from pymince.iterator import centroid

    coord = (((2, 2), (4, 4)))
    tuple(centroid(coord))  # --> (3, 3)
```
##### consume
```
consume(iterator, n=None)

Advance *iterator* by *n* steps. If *n* is ``None``, consume it
entirely.

Examples:
    from pymince.iterator import consume
    it = iter([1, 2])
    consume(it)
    next(it) # --> StopIteration
```
##### grouper
```
grouper(iterable, size)

Make a generator that returns each element being iterable
with "size" as the maximum number of elements.

:param iterable:
:param int size: maximum size of element groups.
:rtype: Generator

Examples:
    from pymince.iterator import grouper

    groups = grouper([1, 2, 3, 4, 5], 2)
    list(list(g) for g in groups) # --> [[1, 2], [3, 4], [5]]
```
##### ibool
```
ibool(iterable)

Iterator class supporting ´__bool__´.

Examples:
    from pymince.iterator import ibool

    it = ibool((1, 2, 3))
    bool(it) # --> True
    list(it) # --> [1, 2, 3]
```
##### in_all
```
in_all(obj, iterables)

Check if the object is contained in all the given iterables.
If the "iterables" are empty, return True.

:param Any obj:
:param iterables: iterable of iterables
:rtype: bool

Examples:
    from pymince.iterator import in_all

    in_all("a", (("a", "b"), "bcd")) # --> False
    in_all("a", (("a", "b"), "abc")) # --> True
    in_all("a", ()) # --> True
```
##### in_any
```
in_any(obj, iterables)

Check if the object is contained in any of the given iterables.

:param Any obj:
:param iterables: iterable of iterables
:rtype: bool

Examples:
    from pymince.iterator import in_any

    in_any("a", (("a", "b"), "bcd")) # --> True
    in_any("a", (("b", "b"), "def")) # --> False
    in_any("a", ()) # --> False
```
##### ipush
```
ipush(iterable)

Iterator class supporting ´append´ and ´prepend´.

Examples:
    from pymince.iterator import ipush

    it = ipush(iter([2, 3])

    it.append(4)
    it.append(5)

    it.prepend(1)
    it.prepend(0)

    list(it)  # --> [0, 1, 2, 3, 4, 5]
```
##### mul
```
mul(iterable, start=1)

Return the multiplication of a 'start' value (default: 1)
plus an iterable of numbers.

When the iterable is empty, return the start value.
```
##### only_one
```
only_one(iterable)

Check if given iterable has only one element.

:param iterable:
:rtype: bool

Examples:
    from pymince.iterator import only_one

    only_one([1]) # --> True
    only_one([1, 2]) # --> False
    only_one([]) # --> False
```
##### pad_end
```
pad_end(iterable, length, fill_value=None)

The function adds "fill_value" at the finishing of the iterable,
until it reaches the specified length.
If the value of the "length" param is less than the length of
the given "iterable", no filling is done.

:param iterable:
:param int length: A number specifying the desired length of the resulting iterable.
:param Any fill_value: Any value to fill the given iterable.
:rtype: Generator

 Examples:
    from pymince.iterator import pad_end

    pad_end(("a", "b"), 3, fill_value="1") # --> "a" "b" "1"
    pad_end(("a", "b"), 3) # --> "a" "b" None
    pad_end(("a", "b", "c"), 3) # --> "a" "b" "c"
```
##### pad_start
```
pad_start(iterable, length, fill_value=None)

The function adds "fill_value" at the beginning of the iterable,
until it reaches the specified length.
If the value of the "length" param is less than the length of
the given "iterable", no filling is done.

:param iterable:
:param int length: A number specifying the desired length of the resulting iterable.
:param Any fill_value: Any value to fill the given iterable.
:rtype: Generator

 Examples:
    from pymince.iterator import pad_start

    pad_start(("a", "b"), 3, fill_value="1") # --> "1" "a" "b"
    pad_start(("a", "b"), 3) # --> None "a" "b"
    pad_start(("a", "b", "c"), 3) # --> "a" "b" "c"
```
##### partition
```
partition(predicate, iterable)

Split the iterable into two lists, based on the boolean return-value
of the predicate.
- (1): items that have predicate(item) == False.
- (2): items that have predicate(item) == True.


Examples:
    from pymince.iterator import partition

    is_odd = lambda x: x % 2 != 0
    even_items, odd_items = partition(is_odd, range(10))  # ([0, 2, 4, 6, 8], [1, 3, 5, 7, 9])
```
##### replacer
```
replacer(iterable, matcher, new_value, count=-1)

Make a generator that yields all occurrences of the old "iterable"
replaced by "new_value".

:param iterable:
:param matcher: Callable to find occurrences. It is an occurrence if the matcher returns True.
:param new_value: Any value to replace found occurrences.
:param int count:
    Maximum number of occurrences to replace.
    -1 (the default value) means replace all occurrences.
:rtype: Generator

Examples:
    from pymince.iterator import replacer

    is_one = lambda n: n == 1
    replacer([1,2,3,1,2,3], is_one, None) # --> None 2 3 None 2 3
    replacer([1,2,3,1,2,3], is_one, None, count=1) # --> None 2 3 1 2 3
```
##### splitter
```
splitter(iterable, sep, key=None, maxsplit=-1, container=None)

Splits an iterable based on a separator.
A separator will never appear in the output.

:param iterable:
:param sep: The delimiter to split the iterable.
:param key
    A function to compare the equality of each element with the given delimiter.
    If the key function is not specified or is None, the element itself is used for compare.
:param maxsplit:
    Maximum number of splits to do.
    -1 (the default value) means no limit.
:param container: Callable to save the splits. By default tuple is used.

:return: Generator with consecutive splits of "iterable" without the delimiter item.

Examples:
    from pymince.iterator import splitter

    data = ("a", "b", "c", "d", "b", "e")
    split_n = splitter(data, "b")  # --> ("a",) ("c", "d") ("e",)
    split_1 = splitter(data, "b", maxsplit=1)  # --> ("a",) ("c", "d", "b", "e")
```
##### sub
```
sub(iterable)

Return the subtraction of a non-empty iterable of numbers and sets.
```
##### truediv
```
truediv(iterable)

Return the division of an non-empty iterable of numbers.
```
##### uniquer
```
uniquer(iterable, key=None)

Make a generator that returns each element from iterable only once
respecting the input order.

Examples:
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

Examples:
    from pymince.iterator import uniques

    uniques([1,2]) # --> True
    uniques([1,1]) # --> False
```
#### json.py
Useful functions for working with JSONs.
##### JSONEncoder
```
JSONEncoder(*, skipkeys=False, ensure_ascii=True, check_circular=True, allow_nan=True, sort_keys=False, indent=None, separators=None, default=None)

JSON encoder that handles additional types compared
to `json.JSONEncoder`

- `datetime` and `date` are serialized to strings according to the isoformat.
- `decimal.Decimal` is serialized to a string.
- `uuid.UUID` is serialized to a string.
- `dataclasses.dataclass` is passed to `dataclasses.asdict`.
- `frozenset` and `set` are serialized by ordering their values.
```
##### dump_from_csv
```
dump_from_csv(csv_path, json_path, /, *, fieldnames=None, start=0, stop=None, strip=True, encoding='utf-8', **kwargs)

Dump CSV file to a JSON file using "utf-8" encoding.

:param str csv_path:
:param str json_path:
:param fieldnames: list of keys for the JSON
:param int start:
    If start is specified, will skip all preceding elements;
    otherwise, start defaults to zero.
:param int stop:
:param bool strip:
    Whether or not white space should be removed from the
    beginning and end of field values.
:param str encoding: utf-8 is used by default.
```
##### dump_into
```
dump_into(filename, payload, encoding='utf-8', **kwargs)

Dump JSON to a file using "utf-8" encoding.

Examples:
    from pymince.json import dump_into

    dump_into("foo.json", {"key": "value"})
```
##### dump_into_zip
```
dump_into_zip(zip_path, arcname, payload, **kwargs)

Dump JSON into the zip archive under the name arcname.

Examples:
    from pymince.json import dump_into_zip

    dump_into_zip("archive.zip", "foo.json", {"key": "value"})
```
##### idump_fork
```
idump_fork(path_items, encoding='utf-8', dump_if_empty=True, **dumps_kwargs)

Incrementally dumps different groups of elements into
the indicated JSON file.
*** Useful to reduce memory consumption ***

:param Iterable[file_path, Iterable[dict]] path_items: group items by file path
:param encoding: 'utf-8' by default.
:param bool dump_if_empty: If false, don't create an empty file.
:param dumps_kwargs: json.dumps kwargs.

Examples:
    from pymince.json import idump_fork

    path_items = (
        ("num.json", ({"value": 1}, {"value": 2})),
        ("num.json", ({"value": 3},)),
        ("foo.json", ({"a": "1"}, {"b": 2})),
        ("baz.json", ()),
    )
    idump_fork(iter(path_items))
```
##### idump_into
```
idump_into(filename, iterable, encoding='utf-8', **kwargs)

Dump an iterable incrementally into a JSON file
using the "utf-8" encoding.
The result will always be an array with the elements of the iterable.
*** Useful to reduce memory consumption ***

Examples:
    from pymince.json import idump_into

    it = iter([{"key": "foo"}, {"key": "bar"}])
    dump_into("foo.json", it)
```
##### idump_lines
```
idump_lines(iterable, **dumps_kwargs)

Generator yielding string lines that form a JSON array
with the serialized elements of given iterable.
*** Useful to reduce memory consumption ***

:param iterable: Iterable[dict]
:rtype: Iterable[str]
```
##### load_from
```
load_from(filename, encoding='utf-8')

Load JSON from a file using "utf-8" encoding.

Examples:
    from pymince.json import load_from

    dictionary = load_from("foo.json")
```
##### load_from_zip
```
load_from_zip(zip_path, arcname)

Load JSON from a file named "arcname" inside a zip archive.

Examples:
    from pymince.json import load_from_zip

    dictionary = load_from_zip("archive.zip", "foo.json")
```
#### jsonlines.py
Useful functions for working with JSON lines data as described:
- http://ndjson.org/
- https://jsonlines.org/
##### dump
```
dump(iterable, fp, **kwargs)

Serialize iterable as a `jsonlines` formatted stream to file.

:param iterable: Iterable[Any]
:param fp: file-like object
:param kwargs: `json.dumps` kwargs

Example:
    from pymince.jsonlines import dump

    data = ({'foo': 1}, {'bar': 2})
    with open('myfile.jsonl', mode='w', encoding ='utf-8') as file:
        dump(iter(data), file)
```
##### dump_fork
```
dump_fork(path_items, encoding='utf-8', dump_if_empty=True, **kwargs)

Incrementally dumps different groups of elements into
the indicated `jsonlines` file.
*** Useful to reduce memory consumption ***

:param Iterable[file_path, Iterable[dict]] path_items: group items by file path
:param encoding: 'utf-8' by default.
:param bool dump_if_empty: If false, don't create an empty `jsonlines` file.
:param kwargs: json.dumps kwargs.

Examples:
    from pymince.jsonlines import dump_fork

    path_items = (
        ("num.jsonl", ({"value": 1}, {"value": 2})),
        ("num.jsonl", ({"value": 3},)),
        ("foo.jsonl", ({"a": "1"}, {"b": 2})),
        ("baz.jsonl", ()),
    )
    dump_fork(iter(path_items))
```
##### dump_into
```
dump_into(filename, iterable, encoding='utf-8', **kwargs)

Dump iterable to a `jsonlines` file.

Example:
    from pymince.jsonlines import dump_into

    data = ({'foo': 1}, {'bar': 2})
    dump_into("myfile.jsonl", iter(data))
```
##### dumper
```
dumper(iterable, **kwargs)

Generator yielding JSON lines.
```
##### dumps
```
dumps(iterable, **kwargs)

Serialize iterable to a `jsonlines` formatted string.

:param iterable: Iterable[Any]
:param kwargs: `json.dumps` kwargs
:rtype: str
```
##### load
```
load(fp, **kwargs)

Returns iterable from a file formatted as JSON lines.

:param fp: file-like object
:param kwargs: `json.loads` kwargs
:rtype: Iterable[str]
```
##### load_from
```
load_from(filename, encoding='utf-8', **kwargs)

Returns iterable from a filename formatted as JSON lines.

:param filename: path
:param encoding: file encoding. 'utf-8' used by default
:param kwargs: `json.loads` kwargs
:rtype: Iterable[str]

Examples:
    from pymince.jsonlines import load_from

    it = load_from("myfile.jsonl")
    next(it)
```
#### logging.py

##### StructuredFormatter
```
StructuredFormatter(fmt=None, datefmt=None, style='%', validate=True)

Implementation of JSON structured logging that works
for most handlers.

Examples:
    import logging
    import sys
    from pymince.logging import StructuredFormatter

    # Config
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)
    formatter = StructuredFormatter('%(message)s')
    handler = logging.StreamHandler(sys.stdout)
    handler.setLevel(logging.DEBUG)
    handler.setFormatter(formatter)
    logger.addHandler(handler)

    # Usage
    logger.debug('', {"string": "value1", "number": 1})
    logger.debug('', {"string": "value2", "number": 2})

    >>Output<<
    {"timestamp":"2022-06-17 18:37:48,789","level":"DEBUG","payload":{"string":"value1","number":1}}
    {"timestamp":"2022-06-17 18:37:48,789","level":"DEBUG","payload":{"string":"value2","number":2}}
```
##### timed_block
```
timed_block(name, logger=None)

Log the duration of the handled context.

Examples:
    import logging
    from pymince.logging import timed_block

    logging.basicConfig(level=logging.DEBUG)
    with timed_block("sleeping"):
        time.sleep(1)

    >>Output<<
    INFO:root:Generating [sleeping]
    DEBUG:root:Finished [sleeping in 1.002 s]
```
#### std.py

##### bind_json_std
```
bind_json_std(encoding='utf-8')

Decorator to call "function" passing the json read from
"stdin" in the keyword parameter "data" and dump the json that the callback returns
to "stdout".

Examples:
from pymince.std import bind_json_std

@bind_json_std()
def foo(data=None):
    print("Processing data from sys.stdin", data)

    result = data and {**data, "new": "value"}

    print("Result to write in sys.stdout", result)
    return result
```
#### text.py
Useful functions for working with strings.
##### are_anagram
```
are_anagram(text1, text2)

Check if two strings are anagram.

Examples:
    from pymince.text import are_anagram

    are_anagram("listen", "silent")      # --> True
    are_anagram("they see", "the eyes")  # --> True
```
##### fullstr
```
fullstr()

Custom string inheriting from "str" which adds
the following methods:

- is_url(self, schemes=None, hostnames=None)
- is_int(self)
- is_positive_int(self)
- is_negative_int(self)
- is_payment_card(self)
- is_binary(self)
- is_percentage(self)
- is_palindrome(self)
- is_email_address(self)
- is_roman(self)
- are_anagram(self, other)
```
##### get_random_secret
```
get_random_secret(length, alphabet='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')

Generate a cryptographically secure random string.
Useful for creating temporary passwords.
```
##### get_random_string
```
get_random_string(length, alphabet='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')

Generate random string.
```
##### is_binary
```
is_binary(text)

Check if the string is binary or not.
```
##### is_email_address
```
is_email_address(text)

Check if the string is an email address.

This solution does a very simple check. It only validates that the string contains an at sign (@)
that is preceded and followed by one or more non whitespace characters.
```
##### is_int
```
is_int(text)

Check if the string is the representation of
a integer number.

True:
 "10",   "10.",   "10.0",
"+10",  "+10.",  "+10.0",
"-10",  "-10.",  "-10.0"
```
##### is_negative_int
```
is_negative_int(text)

Check if the string is the representation of
negative integer number.

True:
"-10",  "-10.",  "-10.0"
```
##### is_palindrome
```
is_palindrome(text)

Check if the string is palindrome or not.
A string is said to be palindrome if the reverse of the string is the same as string
```
##### is_payment_card
```
is_payment_card(text)

Check if the string is a valid payment
card number.

https://en.wikipedia.org/wiki/Payment_card_number#Issuer_identification_number_(IIN)
```
##### is_percentage
```
is_percentage(text)

Check if the string is a valid percentage

True: "100%", "100 %", "100&nbsp;%", 100.0 %",
```
##### is_positive_int
```
is_positive_int(text)

Check if the string is the representation of
positive integer number.

True:
 "10",   "10.",   "10.0",
"+10",  "+10.",  "+10.0",
```
##### is_roman
```
is_roman(text)

Check if the string is a valid roman numeral.
```
##### is_url
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
##### multireplace
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
##### multireplacer
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
##### normalize_newlines
```
normalize_newlines(s)

Normalize CRLF and CR newlines to just LF.
```
##### remove_decimal_zeros
```
remove_decimal_zeros(value, decimal_sep='.', min_decimals=None)

Removes non-significant decimal zeros from a formatted text number.

Examples:
    from pymince.text import remove_decimal_zeros

    remove_decimal_zeros("2.000100", ".") # --> "2.0001"
    remove_decimal_zeros("2.000000", ".") # --> "2"
    remove_decimal_zeros("2.000000", ".", min_decimals=2) # --> "2.00"
```
##### remove_number_commas
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

Examples:
    from pymince.text import replace

    replace("No, woman, no cry", [","], ";") # --> "No; woman; no cry"
    replace("No, woman, no cry", [","], ";", count=1) # --> "No; woman, no cry"
```
#### warnings.py

##### deprecated
```
deprecated(fn)

This is a decorator which can be used to mark functions
as deprecated. It will result in a warning being emitted
when the function is used.
http://code.activestate.com/recipes/391367-deprecated/?in=lang-python

Examples:
    from pymince.warnings import deprecated

    @deprecated
    def check_function():
        pass

    class SomeClass:
        @deprecated
        def check_method(self):
            pass

    @deprecated
    class CheckClass:
        pass

    >> check_function() # DeprecationWarning  --> 'Deprecated "check_function".'
    >> SomeClass().check_method() #  DeprecationWarning --> 'Deprecated "check_method".'
    >> CheckClass() # DeprecationWarning  --> 'Deprecated "CheckClass".'
```
#### xml.py

##### iterparse
```
iterparse(filename)

Incrementally parse XML document into ElementTree.

This function is based on: https://github.com/python/cpython/issues/93618

'Fix misleading hint for original ElementTree.iterparse.'
'''
The code below deletes a root child once it is completed, then processes and removes
it from the memory (if nothing more references to it ofc).
This allows to process 7GB XML with with a memory usage up to 10MB (in case of great number of root children).
'''

:param str filename: XML filename
:rtype: Generator

 Examples:
    from pymince.xml import iterparse

    for event, obj in iterparse("countries.xml")
        if event == 'start'
            print(obj, obj.tag, obj.attrib, obj.text)

    >>Output<<
    <Element 'country' at 0x0000018ADF9D0CC0> country {'code': 'as', 'iso': '16'} American Samoa
    <Element 'country' at 0x0000018ADF9D0C70> country {'code': 'ad', 'iso': '20'} Andorra
```
### Upgrade README.md

Upgrade README.md `Usage` section according to current *pymince* code.
```
(env) python upgrade_readme_usage.py
```
