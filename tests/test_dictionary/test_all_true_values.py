import pytest

import pymince.dictionary


@pytest.mark.parametrize(
    "dictionary,keys,expected",
    [
        ({}, ("a",), False),
        ({"a": 1}, ("b",), False),
        ({"a": 1}, ("a",), True),
        ({"a": 1, "b": None}, ("a",), True),
        ({"a": 1, "b": 1}, ("a", "b"), True),
        ({"a": 1, "b": None}, ("a", "b"), False),
    ]
)
def test_all_keys_and_values(dictionary, keys, expected):
    result = pymince.dictionary.all_true_values(dictionary, keys)
    assert result == expected
