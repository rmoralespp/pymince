import collections
import operator

import pytest

import pymince.dictionary


def test_dict_from_iterable_with_func_getter():
    values = iter([1, 2, 3])
    result = pymince.dictionary.dict_from_iterable(values, lambda n: n, lambda n: n ** 2)
    assert result == {1: 1, 2: 4, 3: 9}


def test_dict_from_iterable_with_itemgetter_index():
    keygetter = operator.itemgetter(0)
    valgetter = operator.itemgetter(1, 2)
    values = iter([(1, "a", "b"), (2, "a", "b")])
    result = pymince.dictionary.dict_from_iterable(values, keygetter, valgetter)
    assert result == {1: ('a', 'b'), 2: ('a', 'b')}


def test_dict_from_iterable_with_itemgetter_name():
    keygetter = operator.itemgetter("i")
    valgetter = operator.itemgetter("v")
    values = iter([{"i": 0, "v": "foo1"}, {"i": 1, "v": "foo2"}])
    result = pymince.dictionary.dict_from_iterable(values, keygetter, valgetter)
    assert result == {0: 'foo1', 1: 'foo2'}


def test_dict_from_iterable_with_attrgetter_name():
    Person = collections.namedtuple("Person", ["name", "year"])
    keygetter = operator.attrgetter("name")
    valgetter = operator.attrgetter("year")
    values = iter([Person(name="Foo", year=2022), Person(name="Foo1", year=2023)])
    result = pymince.dictionary.dict_from_iterable(values, keygetter, valgetter)
    assert result == {'Foo': 2022, 'Foo1': 2023}


def test_dict_from_iterable_with_duplicated_key():
    keygetter = operator.itemgetter(0)
    valgetter = operator.itemgetter(1)
    values = iter([["a", 1], ["a", 2], ["b", 3]])

    with pytest.raises(ValueError):
        pymince.dictionary.dict_from_iterable(values, keygetter, valgetter)
