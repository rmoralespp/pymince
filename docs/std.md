# Std
Standard library utilities.

**bind_json_std**
```
bind_json_std(encoding='utf-8')

Decorator to call "function" passing the json read from
"stdin" in the keyword parameter "data" and dump the json that the callback returns
to "stdout".

Examples:
from pymince.std import bind_json_std

@bind_json_std()
def foo(data=None):
    print("Processing data from sys.stdin", data)

    result = data and {**data, "new": "value"}

    print("Result to write in sys.stdout", result)
    return result
```