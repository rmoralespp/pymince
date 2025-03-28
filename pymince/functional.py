# -*- coding: utf-8 -*-

"""Functional programming utilities."""

import contextlib
import functools
import time


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

    def getter(self, method):
        """Descriptor to change the getter on a classproperty."""

        self.fget = method
        return self


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
        inc_once()  #  → 'anything'
        inc_once()  #  → 'anything'
        inc_once()  #  → 'anything'
        print(n)    #  → 1
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


def caller(*args, **kwargs):
    """
    Return a callable that calls with given params.

    Examples:
        import pymince.functional

        caller = pymince.functional.caller(range(5))
        caller(len)   #  5
        caller(list)  # [0, 1, 2, 3, 4]
    """

    return lambda f: f(*args, **kwargs)


def suppress(*exceptions, default=None):
    """
    Decorator to suppress the specified exceptions and return the
    default value instead.

    Examples:
        from pymince.functional import suppress

        @suppress(FileNotFoundError, default=False)
        def remove(somefile):
             os.remove(somefile)

        remove("no_found.txt")  # False
    """

    def decorator(fn):
        @functools.wraps(fn)
        def wrapper(*args, **kwargs):
            with contextlib.suppress(*exceptions):
                return fn(*args, **kwargs)
            return default

        return wrapper

    return decorator


def retry_when(delay=0, tries=1, condition=lambda x: x is None):
    """
    Decorator that retries executing the wrapped function based on a condition.

    :param int delay: Seconds delay between attempts. Default: 0.
    :param int tries: Number of attempts. Default: 1
    :param Callable condition: Function that returns True if the function should be retried.
                      By default, it retries if the result is None.
    :return: The result of the wrapped function after the final attempt.

    Examples:
        @retry_when(delay=0, tries=1)
        def foo():
            return 1
    """

    if tries <= 0:
        raise ValueError("'tries' must be greater than to 0")

    def decorator(function):
        @functools.wraps(function)
        def apply(*args, **kwargs):
            for _ in range(tries):
                result = function(*args, **kwargs)
                if not condition(result):
                    break
                if delay:  # Avoid sleeping after the attempt
                    time.sleep(delay)
            return result

        return apply

    return decorator


def retry_if_errors(*exceptions, delay=0, tries=1):
    """
    Decorator that retries to call the wrapped function
    if any of given exceptions are thrown.

    :param exceptions: Lists of exceptions that trigger a retry attempt.
    :param int delay: Seconds delay between attempts. Default is 0.
    :param int tries: Number of attempts. Default is 1.
    :return: The result of the wrapped function after the final attempt.

    Examples:
    @retry_if_errors(ValueError, TypeError, delay=0, tries=1)
    def foo():
        return 1
    """

    if tries <= 0:
        raise ValueError("'tries' must be greater than to 0")

    def decorator(function):
        @functools.wraps(function)
        def apply(*args, **kwargs):
            for _ in range(tries):
                try:
                    return function(*args, **kwargs)
                except exceptions:
                    if delay:  # Avoid sleeping after the attempt
                        time.sleep(delay)

            raise ValueError(f"Failed after {tries} attempts")

        return apply

    return decorator


def identity(x):
    """
    Takes a single argument and returns it unchanged.
    Identity function, as defined in https://en.wikipedia.org/wiki/Identity_function.
    """

    return x
