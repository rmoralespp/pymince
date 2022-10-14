import pytest

import pymince.functional


def test_instancemethod():
    class MyClass:

        def __init__(self):
            self._foo = "var"

        @pymince.functional.classproperty
        def foo(self):
            return self._foo

    with pytest.raises(AttributeError):
        assert MyClass.foo


def test_classmethod():
    class MyClass:
        _foo = "var"

        @pymince.functional.classproperty
        def foo(cls):
            return cls._foo

    assert MyClass.foo == "var"


def test_classmethod_with_params():
    class MyClass:

        @pymince.functional.classproperty
        def foo(cls, *args, **kwargs):
            return args, kwargs

    with pytest.raises(TypeError):
        assert MyClass.foo("a", b="b")
