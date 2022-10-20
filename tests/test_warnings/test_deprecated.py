import warnings

import pymince.warnings


def assert_warning(w, expected_warning_msg):
    assert len(w) == 1
    assert issubclass(w[-1].category, DeprecationWarning)
    assert str(w[-1].message) == expected_warning_msg


def test_function():
    @pymince.warnings.deprecated
    def some_function(a, b):
        return a + b

    with warnings.catch_warnings(record=True) as w:
        warnings.simplefilter("always")  # Cause all warnings to always be triggered.
        res = some_function(1, 2)  # Trigger a warning.

    assert_warning(w, 'Deprecated "some_function".')
    assert res == 3


def test_method():
    class SomeClass:

        @pymince.warnings.deprecated
        def some_method(self, x, y):
            return x + y

    with warnings.catch_warnings(record=True) as w:
        warnings.simplefilter("always")  # Cause all warnings to always be triggered.
        res = SomeClass().some_method(2, 3)  # Trigger a warning.

    assert_warning(w, 'Deprecated "some_method".')
    assert res == 5


def test_class():
    @pymince.warnings.deprecated
    class SomeClass:
        pass

    with warnings.catch_warnings(record=True) as w:
        warnings.simplefilter("always")  # Cause all warnings to always be triggered.
        _ = SomeClass()  # Trigger a warning.

    assert_warning(w, 'Deprecated "SomeClass".')
