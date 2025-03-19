# -*- coding: utf-8 -*-

import pymince.patterns


class MyClass(metaclass=pymince.patterns.Singleton):
    pass


def test_singleton():
    assert MyClass() is MyClass()
