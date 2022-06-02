import datetime
import enum
import functools
import hashlib
import json


def find_nested_key(key, dictionary):
    """
    Find key in dictionary.

    egg:
    * find_nested_key('a', {}) -> 'a'
    * find_nested_key('a', {'a': 'b', 'b': 'c'}) -> 'c'
    * find_nested_key('a', {'a': 'a'}) -> 'a'
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
    """Calculate a digest of a "jsonified" python dictionary."""

    def __init__(self, include_keys=None, exclude_keys=None):
        if include_keys and exclude_keys:
            raise ValueError
        self.include = include_keys and frozenset(include_keys)
        self.exclude = exclude_keys and frozenset(exclude_keys)

    def __call__(self, dictionary):
        string = self.to_string(dictionary)
        return hashlib.md5(string.encode('utf-8')).hexdigest()

    @functools.cached_property
    def jsonify(self):
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
        return self.jsonify(data)
