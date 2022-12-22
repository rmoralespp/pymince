"""Useful functions that use dictionaries."""

import datetime
import enum
import functools
import hashlib
import json
import operator
import types


def all_true_values(dictionary, keys):
    """
    Check if an dictionary has all specified keys and
    key-related values as True.

    :param dict dictionary:
    :param keys: keys sequence
    :rtype: bool

    Examples:
    from pymince.dictionary import all_true_values

    all_true_values({"a": 1, "b": 2}, ("a", "b")) # --> True
    all_true_values({"a": 1, "b": 0}, ("a", "b")) # --> False
    all_true_values({"a": 1, "b": 0}, ("a",)) # --> True
    """

    getter = operator.itemgetter(*keys)
    try:
        values = getter(dictionary)
    except KeyError:
        return False
    else:
        return all(values) if len(keys) > 1 else bool(values)


def find_leaf_value(key, dictionary):
    """
    Find leaf value in mapping.

    :param str key:
    :param dict dictionary:

    Examples:
        from pymince.dictionary import find_leaf_value

        find_leaf_value('a', {}) # --> 'a'
        find_leaf_value('a', {'a': 'b', 'b': 'c'}) # --> 'c'
        find_leaf_value('a', {'a': 'a'}) # --> 'a'
    """
    while True:
        if key is not None and key in dictionary:
            new_key = dictionary[key]
            if new_key == key:
                break
            key = new_key
        else:
            break
    return key


class DigestGetter:
    """
    Calculate a digest of a "jsonified" python dictionary.

    :param include_keys: dictionary keys to exclude
    :param exclude_keys: dictionary keys to include
    :rtype: str

    Examples:
        from pymince.dictionary import DigestGetter

        getter = DigestGetter(include_keys=("a",))
        getter({"a": 1, "b": 1}) # --> bb6cb5c68df4652941caf652a366f2d8
        getter({"a": 1}) # --> bb6cb5c68df4652941caf652a366f2d8
    """

    def __init__(self, include_keys=None, exclude_keys=None):
        if include_keys and exclude_keys:
            raise ValueError
        self.include = include_keys and frozenset(include_keys)
        self.exclude = exclude_keys and frozenset(exclude_keys)

    def __call__(self, dictionary):
        string = self.to_string(dictionary)
        return hashlib.md5(string.encode('utf-8')).hexdigest()

    @functools.cached_property
    def stringify(self):
        """
        Return a function to encode a dict into json using the most compact form.
        Dictionary keys are sorted.
        Encodes datetime objects into isoformat strings.
        Encodes enum objects according to "value" attribute.
        Encode sets by ordering their values.
        """

        class Encoder(json.JSONEncoder):
            def default(self, obj):
                if isinstance(obj, datetime.datetime):
                    return obj.isoformat()
                elif isinstance(obj, enum.Enum):
                    return obj.value
                elif isinstance(obj, (frozenset, set)):
                    return sorted(obj)
                else:
                    return super().default(obj)

        return Encoder(
            separators=(',', ':'),
            check_circular=False,
            sort_keys=True,
            ensure_ascii=False
        ).encode

    def to_string(self, dictionary):
        # Non recursive copy.
        if self.include:
            data = {k: v for k, v in dictionary.items() if k in self.include}
        elif self.exclude:
            data = {k: v for k, v in dictionary.items() if k not in self.exclude}
        else:
            data = dictionary
        return self.stringify(data)


def frozendict(*args, **kwargs):
    """
    Returns a "MappingProxyType" from a dictionary built according to given parameters.
    Add immutability only on a first level.

    Examples:
        from pymince.dictionary import frozendict

        my_dict = frozendict(a=1, b=2)
        my_dict["a"] # --> 1
        list(my_dict.items())  # --> [("a", 1), ("b", 2)]
        my_dict["c"] = 3  # --> TypeError
    """
    return types.MappingProxyType(dict(*args, **kwargs))


def from_objects(iterable, key_getter, value_getter):
    """
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
    """

    dictionary = {}
    for obj in iter(iterable):
        key = key_getter(obj)
        if key in dictionary:
            raise ValueError
        else:
            dictionary[key] = value_getter(obj)
    return dictionary
