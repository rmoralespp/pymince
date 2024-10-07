# dictionary.py
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