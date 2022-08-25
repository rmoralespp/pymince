import functools
import time


def retry_if_none(delay=0, tries=1):
    """
    Decorator that retries to call the wrapped function
    if it returns None.

    :param int delay: seconds delay between attempts. default: 0.
    :param int tries: number of attempts. default: 1

    Examples:
        @retry_if_none(delay=0, tries=1)
        def foo():
            return 1
    """

    def decorator(function):
        @functools.wraps(function)
        def apply(*args, **kwargs):
            attempt = 0
            result = None
            while attempt < tries and result is None:
                time.sleep(delay)
                result = function(*args, **kwargs)
                attempt += 1
            return result

        return apply

    return decorator


def retry_if_errors(*exceptions, delay=0, tries=1):
    """
    Decorator that retries to call the wrapped function
    if any of given exceptions are thrown.

    :param exceptions: Lists of exceptions that trigger a retry attempt.
    :param int delay: seconds delay between attempts. default: 0.
    :param int tries: number of attempts. default: 1

    Examples:
    @retry_if_errors(ValueError, TypeError, delay=0, tries=1)
    def foo():
        return 1
    """

    def decorator(function):
        def apply(*args, **kwargs):
            attempt = 0
            while attempt < tries:
                time.sleep(delay)
                try:
                    return function(*args, **kwargs)
                except exceptions:
                    attempt += 1
            return function(*args, **kwargs)

        return apply

    return decorator
