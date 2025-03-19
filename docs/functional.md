# Functional
Functional programming utilities.

**caller**
```
caller(*args, **kwargs)

Return a callable that calls with given params.

Examples:
    import pymince.functional

    caller = pymince.functional.caller(range(5))
    caller(len)   #  5
    caller(list)  # [0, 1, 2, 3, 4]
```
**classproperty**
```
classproperty(method=None)

Decorator that converts a method with a single cls argument into a property
that can be accessed directly from the class.

Examples:
    from pymince.functional import classproperty

    class MyClass:
        __foo = "var"

        @classproperty
        def foo(cls):
            return cls.__foo
```
**identity**
```
identity(x)

Takes a single argument and returns it unchanged.
Identity function, as defined in https://en.wikipedia.org/wiki/Identity_function.
```
**once**
```
once(fn)

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
```
**pipe**
```
pipe(*fns)

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
```
**retry_if_errors**
```
retry_if_errors(*exceptions, delay=0, tries=1)

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
```
**retry_when**
```
retry_when(delay=0, tries=1, condition=<function <lambda> at 0x0000023520A3F9C0>)

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
```
**set_attributes**
```
set_attributes(**kwargs)

Decorator to set attributes on functions and classes.

Examples:
    from pymince.functional import set_attributes

    @set_attributes(short_description="dummy function")
    def foo():
        pass

    print(foo.short_description)  # "dummy function"

Based on: https://github.com/wolph/python-utils/ (set_attributes)
```
**suppress**
```
suppress(*exceptions, default=None)

Decorator to suppress the specified exceptions and return the
default value instead.

Examples:
    from pymince.functional import suppress

    @suppress(FileNotFoundError, default=False)
    def remove(somefile):
         os.remove(somefile)

    remove("no_found.txt")  # False
```