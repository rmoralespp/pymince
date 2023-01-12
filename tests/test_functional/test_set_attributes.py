# -*- coding: utf-8 -*-
import pymince.functional


def test_set_attributes():
    @pymince.functional.set_attributes(lang="en", date="2022-12-12")
    def foo():
        return "foo"

    assert foo.__name__ == "foo"
    assert foo.lang == "en"
    assert foo.date == "2022-12-12"


def test_set_name():
    @pymince.functional.set_attributes(__name__="new_name")
    def old_name():
        pass

    assert old_name.__name__ == "new_name"


def test_result():
    @pymince.functional.set_attributes(foo="a")
    def foo(p):
        return p

    assert foo("abcb") == "abcb"
