import functools
import json
import operator
import sys

import pymince.json


def bind_json_std(encoding="utf-8"):
    """
    Decorator to call "function" passing the json read from
    "stdin" in the keyword parameter "data" and dump the json that the callback returns
    to "stdout".
    """

    def decorator(function):
        @functools.wraps(function)
        def apply(*args, **kwargs):
            encode_std = operator.methodcaller("reconfigure", encoding=encoding)

            encode_std(sys.stdin)
            encode_std(sys.stdout)

            data = json.load(sys.stdin)
            resp = function(*args, **kwargs, data=data)
            if resp:
                pymince.json.dump(resp, sys.stdout)

        return apply

    return decorator
