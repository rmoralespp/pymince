import pytest

import pymince.dictionary


def test_get_item():
    my_dict = pymince.dictionary.frozendict(a=1, b=2)
    assert my_dict["a"] == 1


def test_contains_key():
    my_dict = pymince.dictionary.frozendict(a=1, b=2)
    assert "b" in my_dict


def test_set_item():
    my_dict = pymince.dictionary.frozendict(a=1, b=2)
    with pytest.raises(TypeError):
        my_dict["a"] = 1


def test_del_item():
    my_dict = pymince.dictionary.frozendict(a=1, b=2)
    with pytest.raises(TypeError):
        del my_dict["a"]


def test_not_immutable():
    my_dict = pymince.dictionary.frozendict(a=1, b={"c": 1})
    my_dict["b"]["c"] = 2
    assert dict(my_dict) == {'a': 1, 'b': {'c': 2}}
