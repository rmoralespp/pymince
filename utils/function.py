import time


def retry_if_none(delay=0, tries=1):
    """
    Returns a retry decorator if the callback
    returns None.

    :param int delay: seconds delay between attempts. default: 0.
    :param int tries: number of attempts. default: 1
    """

    def decorator(function):
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
