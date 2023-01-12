# -*- coding: utf-8 -*-
import functools


class classproperty:
    """
    Decorator that converts a method with a single cls argument into a property
    that can be accessed directly from the class.

    Examples:
        from pymince.functional import classproperty

        class MyClass:
            __foo = "var"

            @classproperty
            def foo(cls):
                return cls.__foo
    """

    def __init__(self, method=None):
        self.fget = method

    def __get__(self, instance, cls=None):
        return self.fget(cls)


def pipe(*fns):
    """
    Compose functions from left to right.

    :param fns: Functions to compose.
    :rtype: Callable[[Any], Any]

    Examples:
        from pymince.functional import pipe

        addtwo = lambda n: n + 2
        double = lambda n: n * 2
        square = lambda n: n * n

        fn = pipe(addtwo, double, square)
        fn(1) # --> 36
    """

    def wrap(arg):
        return functools.reduce(lambda v, fn: fn(v), fns, arg)

    return wrap


def once(fn):
    """
    Decorator to execute a function only once.

    Examples:
        from pymince.functional import once

        @once
        def inc_once():
            global n
            n += 1
            return 'anything'

        n = 0
        inc_once()  #  --> 'anything'
        inc_once()  #  --> 'anything'
        inc_once()  #  --> 'anything'
        print(n)    #  --> 1
    """

    @functools.wraps(fn)
    def decorator(*args, **kwargs):
        if not hasattr(decorator, 'ran'):
            decorator.ran = fn(*args, **kwargs)
        return decorator.ran

    return decorator


def set_attributes(**kwargs):
    """
    Decorator to set attributes on functions and classes.

    Examples:
        from pymince.functional import set_attributes

        @set_attributes(short_description="dummy function")
        def foo():
            pass

        print(foo.short_description)  # "dummy function"

    Based on: https://github.com/wolph/python-utils/ (set_attributes)
    """

    def wrap(fn):
        for key, value in kwargs.items():
            setattr(fn, key, value)
        return fn

    return wrap
