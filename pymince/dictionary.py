import datetime
import enum
import functools
import hashlib
import json
import operator


def all_true_values(dictionary, keys):
    """
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
    """

    getter = operator.itemgetter(*keys)
    try:
        values = getter(dictionary)
    except KeyError:
        return False
    else:
        return all(values) if len(keys) > 1 else bool(values)


def key_or_leaf_value(key, dictionary):
    """
    Find leaf key in dictionary.

    :param str key: Key to find.
    :param dict dictionary:

    Usage:
        from pymince.dictionary import key_or_leaf_value

        key_or_leaf_value('a', {}) # --> 'a'
        key_or_leaf_value('a', {'a': 'b', 'b': 'c'}) # --> 'c'
        key_or_leaf_value('a', {'a': 'a'}) # --> 'a'
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

    Usage:
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
                elif isinstance(obj, set):
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
