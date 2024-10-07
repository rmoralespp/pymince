# warnings.py

##### deprecated
```
deprecated(fn)

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
```