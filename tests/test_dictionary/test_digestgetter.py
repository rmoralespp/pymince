import datetime
import enum

import pytest

import pymince.dictionary


@pytest.fixture()
def payload():
    class MyEnum(enum.Enum):
        foo = "foo"

    return {
        "numb": 1.0,
        "date": datetime.datetime(2021, 1, 1),
        "text": "ñó",
        "enum": MyEnum.foo,
        "set": {"a", "b"}
    }


def test_to_string(payload):
    expected = '{"date":"2021-01-01T00:00:00","enum":"foo","numb":1.0,"set":["a","b"],"text":"ñó"}'
    res = pymince.dictionary.DigestGetter().to_string(payload)
    assert res == expected


def test_to_string_include(payload):
    expected = '{"text":"ñó"}'
    res = pymince.dictionary.DigestGetter(include_keys=("text",)).to_string(payload)
    assert res == expected


def test_to_string_exclude(payload):
    expected = '{"date":"2021-01-01T00:00:00","enum":"foo","numb":1.0,"set":["a","b"]}'
    res = pymince.dictionary.DigestGetter(exclude_keys=("text",)).to_string(payload)
    assert res == expected


def test_digest(payload):
    expected = '735bf119e94b46591918c1b0115efa04'
    res = pymince.dictionary.DigestGetter()(payload)
    assert res == expected


def test_digest_include(payload):
    expected = '7a439974e23327ec0c28c990e49f6d51'
    res = pymince.dictionary.DigestGetter(include_keys=("text",))(payload)
    assert res == expected


def test_digest_exclude(payload):
    expected = '55b0acefacd6b0614cb5e4ec8506db0a'
    res = pymince.dictionary.DigestGetter(exclude_keys=("text",))(payload)
    assert res == expected


def test_digest_with_value_error():
    with pytest.raises(ValueError):
        pymince.dictionary.DigestGetter(include_keys=("a",), exclude_keys=("a",))
