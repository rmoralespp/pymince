# -*- coding: utf-8 -*-

import functools
import warnings


def deprecated(fn):
    """
    This is a decorator which can be used to mark functions
    as deprecated. It will result in a warning being emitted
    when the function is used.
    http://code.activestate.com/recipes/391367-deprecated/?in=lang-python

    Examples:
        from pymince.warnings import deprecated

        @deprecated
        def check_function():
            pass

        class SomeClass:
            @deprecated
            def check_method(self):
                pass

        @deprecated
        class CheckClass:
            pass

        >> check_function() # DeprecationWarning  --> 'Deprecated "check_function".'
        >> SomeClass().check_method() #  DeprecationWarning --> 'Deprecated "check_method".'
        >> CheckClass() # DeprecationWarning  --> 'Deprecated "CheckClass".'
    """

    @functools.wraps(fn)
    def wrapper(*args, **kwargs):
        warnings.warn(
            'Deprecated "%s".' % fn.__name__,
            category=DeprecationWarning,
            stacklevel=2)

        # stacklevel=2. The printed warning will indicate and show the call site to the deprecated
        # function rather than to the location of the warnings.warn() call.
        return fn(*args, **kwargs)

    return wrapper
