# -*- coding: utf-8 -*-

import pymince.functional

suppressed = object()


def test_suppress():
    @pymince.functional.suppress(ValueError)
    def to_int():
        return int("foo")

    assert to_int.__name__ == "to_int"
    assert not to_int()


def test_suppress_with_default():
    @pymince.functional.suppress(KeyError, default=suppressed)
    def get_a(dictionary):
        return dictionary["a"]

    assert get_a.__name__ == "get_a"
    assert get_a({}) is suppressed


def test_suppress_with_multi_errors():
    @pymince.functional.suppress(KeyError, ValueError, default=suppressed)
    def get_a(dictionary):
        return dictionary["a"]

    assert get_a.__name__ == "get_a"
    assert get_a({}) is suppressed
