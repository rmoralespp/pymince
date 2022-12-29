# -*- coding: utf-8 -*-
import pymince.functional


def test_call():
    n = 0

    @pymince.functional.once
    def my_func():
        nonlocal n
        n += 1
        return True

    assert my_func()
    assert n == 1


def test_many_calls():
    n = 0
    expected = result = "foo"

    @pymince.functional.once
    def my_func():
        nonlocal n
        n += 1
        return result

    for _i in range(10):
        assert my_func() == expected
    assert n == 1


def test_many_calls_with_mutable_arg():
    container = []

    @pymince.functional.once
    def my_func(n):
        n.append(1)
        return True

    for _i in range(10):
        assert my_func(container)
    assert container == [1]


def test_ran_attribute_after_call():
    @pymince.functional.once
    def my_func():
        return 'foo'

    my_func()
    assert my_func.ran == 'foo'


def test_ran_attr_before_call():
    @pymince.functional.once
    def my_func():
        return 'foo'

    assert not hasattr(my_func, 'ran')


def test_func_name():
    @pymince.functional.once
    def my_func():
        pass

    assert my_func.__name__ == 'my_func'
