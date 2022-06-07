# pymince

[![CI](https://github.com/rmoralespp/pymince/workflows/CI/badge.svg)](https://github.com/rmoralespp/pymince/actions?query=event%3Arelease+workflow%3ACI)
[![pypi](https://img.shields.io/pypi/v/pymince.svg)](https://pypi.python.org/pypi/pymince)
[![versions](https://img.shields.io/pypi/pyversions/pymince.svg)](https://github.com/rmoralespp/pymince)


### About
pymince is a collection of useful tools that are "missing" from the Python standard library.

### Installation (via pip)

```pip install pymince```

### Tests

```
(env)$ pip install -r requirements.txt   # Ignore this command if it has already been executed
(env)$ pytest tests/
```

### Usage

#### dictionary.py
##### DigestGetter
```
DigestGetter(include_keys=None, exclude_keys=None)

Calculate a digest of a "jsonified" python dictionary.

Usage:
>> getter = DigestGetter(include_keys=("a",))
>> getter({"a": 1, "b": 1}) # bb6cb5c68df4652941caf652a366f2d8
>> getter({"a": 1}) # bb6cb5c68df4652941caf652a366f2d8
```
##### all_true_values
```
all_true_values(dictionary, keys)

Check if an dictionary has all specified keys and
key-related values as True.

:param dict dictionary:
:param keys: keys sequence
:rtype: bool
```
##### key_or_leaf_value
```
key_or_leaf_value(key, dictionary)

Find leaf key in dictionary.

:param str key: Key to find.
:param dict dictionary:

Usage:
* key_or_leaf_value('a', {}) -> 'a'
* key_or_leaf_value('a', {'a': 'b', 'b': 'c'}) -> 'c'
* key_or_leaf_value('a', {'a': 'a'}) -> 'a'
```
#### file.py
##### ensure_directory
```
ensure_directory(path, cleaning=False)

Make sure the given file structure is an existing directory.
If it does not exist, a new directory will be created.

:param str path:
:param bool cleaning:
    If "cleaning" is True and the directory already exists,
    existing content will be deleted.
```
##### match_on_zip
```
match_on_zip(zip_file, pattern)

Make an iterator that returns file names in the zip file that
match the given pattern.

:param zip_file: instance of ZipFile class
:param pattern: Callable to filter filename list
```
##### open_on_zip
```
open_on_zip(zip_file, filename)

Open a file that is inside a zip file.

Usage:
-------------------------------------------------
import zipfile
with zipfile.ZipFile(zip_filename) as zf:
    # example1
    with open_on_zip(zf, "foo1.txt") as fd1:
        foo1_string = fd1.read()
    # example2
    with open_on_zip(zf, "foo2.txt") as fd2:
        foo2_string = fd2.read()
-------------------------------------------------
```
#### iterator.py
##### all_distinct
```
all_distinct(iterable, key=None)

Check if all the elements of a key-based iterable are distinct.

:param iterable:
:param key: None or "Callable" to compare if iterable items.
:rtype: bool

Usage:
>> all_distinct([1, 1]) --> False
>> all_distinct([1, 2]) --> True
```
##### all_equal
```
all_equal(iterable, key=None)

Check if all the elements of a key-based iterable are equals.

:param iterable:
:param key: None or "Callable" to compare if iterable items.
:rtype: bool

Usage:
>> all_equal([1, 1]) --> True
>> all_equal([1, 2]) --> False
```
##### consume
```
consume(iterator)

Completely consume the given iterator.
```
##### grouper
```
grouper(iterable, size)

Make an iterator that returns each element being iterable
with "size" as the maximum number of elements.

:param iterable:
:param int size: maximum size of element groups.

Usage:
>> list(list(g) for g in grouper([1, 2, 3, 4, 5])) == [[1, 2], [3, 4], [5]]
```
##### is_only_one
```
is_only_one(iterable)

Check if given iterable has only one element.

:param iterable:
:rtype: bool
```
##### non_empty_or_none
```
non_empty_or_none(iterator)

Returns an non-empty iterator or None according to given "iterator".

:param iterator:
:return: Iterator or None

Usage:
>> non_empty_or_none([]) --> None
>> non_empty_or_none([1,2]) --> 1 2
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
>> replacer([1,2,3,1,2,3], lambda n: n == 1, None) --> None 2 3 None 2 3
>> replacer([1,2,3,1,2,3], lambda n: n == 1, None, count=1) --> None 2 3 1 2 3
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
>> data = ["a", "b", "c", "d", "b", "e"]
>> list(list(s) for s in splitter(data, "b")) --> [["a"], ["c", "d"], ["e"]]
>> list(list(s) for s in splitter(data, "b"), maxsplit=1) --> [["a"], ["c", "d", "b", "e"]]
```
##### uniquer
```
uniquer(iterable, key=None)

Make an iterator that returns each element from iterable only once
respecting the input order.
```
##### uniques
```
uniques(iterable, key=None)

Check if all the elements of a key-based iterable are unique.

:param iterable:
:param key: None or "Callable" to compare if iterable items.
:rtype: bool

Usage:
>> uniques([1,2]) --> True
>> uniques([1,1]) --> False
```
#### json.py
##### dump_into
```
dump_into(filename, payload, indent=2)

Dump JSON to a file.

Usage:
>> dump_into("foo.json", {"key": "value"})
```
##### load_from
```
load_from(filename)

Load JSON from a file.

Usage:
>> dictionary = load_from("foo.json")
```
#### logging.py
##### timed_block
```
timed_block(name)

Logger the duration of the handled context.

Usage:
>> logging.basicConfig(level=logging.DEBUG)
>> with timed_block("sleeping"):
    >> time.sleep(1)

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
### Upgrade README.md

Upgrade README.md `Usage` section according to current *pymince* code.
```
(env) python upgrade_readme_usage.py
```
