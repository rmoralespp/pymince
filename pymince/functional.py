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
    Simple pipe function implementation using function composition.

    :param fns: Functions to pipe.
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
