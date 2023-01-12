# -*- coding: utf-8 -*-
import dataclasses
import datetime
import decimal
import enum
import uuid

import pytest

import pymince.json


def test_encode_basic():
    data = {"int": 1, "float": 1.2, "tuple": ("a", "b"), "list": [1, 2], "string": "foo", "dict": {"a": 1}}
    expected = '{"int": 1, "float": 1.2, "tuple": ["a", "b"], "list": [1, 2], "string": "foo", "dict": {"a": 1}}'
    res = pymince.json.JSONEncoder().encode(data)
    assert res == expected


def test_encode_dates():
    dates = {"date": datetime.date(2023, 1, 1), "datetime": datetime.datetime(2023, 1, 1)}
    expected = '{"date": "2023-01-01", "datetime": "2023-01-01T00:00:00"}'
    res = pymince.json.JSONEncoder().encode(dates)
    assert res == expected


def test_encode_sets():
    unsorted_chars = "bcadgt"
    sets = {"set": set(unsorted_chars), "frozenset": frozenset(unsorted_chars)}
    expected = '{"set": ["a", "b", "c", "d", "g", "t"], "frozenset": ["a", "b", "c", "d", "g", "t"]}'
    res = pymince.json.JSONEncoder().encode(sets)
    assert res == expected


def test_encode_decimal():
    dec = decimal.Decimal(3.14)
    expected = '{"decimal": "3.140000000000000124344978758017532527446746826171875"}'
    res = pymince.json.JSONEncoder().encode({"decimal": dec})
    assert res == expected


def test_encode_uuid():
    uuid4 = uuid.uuid4()
    expected = f'{{"uuid": "{str(uuid4)}"}}'
    res = pymince.json.JSONEncoder().encode({"uuid": uuid4})
    assert res == expected


def test_encode_dataclass():
    @dataclasses.dataclass
    class Foo:
        a: int
        b: str

    expected = '{"data": {"a": 1, "b": "abc"}}'
    res = pymince.json.JSONEncoder().encode({"data": Foo(a=1, b="abc")})
    assert res == expected


def test_unsupported():
    class MyEnum(enum.Enum):
        foo = "foo"

    with pytest.raises(TypeError):
        pymince.json.JSONEncoder().encode({"enum": MyEnum.foo})
