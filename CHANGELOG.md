## In Progress ##

- **Changed:** retry.retry_if_errors. Used `functools.wraps` to apply update_wrapper.
- **Changed:** file.decompress. Added `size` arg.
- **Changed:** Purpose of `n` arg of algorithm.fibonacci.
- **Changed:** json.dump_into, json.dump_into_zip, json.dump_from_csv. Pass **kwargs to `json.dump/s`

## v2.3.0 (2023-01-13) ##

- **Added:** iterator.mul, iterator.truediv, iterator.sub
- **Added:** functional.set_attributes
- **Added:** json.JSONEncoder. Handles additional types compared to `json.JSONEncoder`
- **Changed:** dictionary.DigestGetter. Now does not support enums and uses the new `pymince.json.JSONEncoder`.

## v2.2.1 (2023-01-12) ##

- **Fixed:** README

## v2.2.0 (2023-01-12) ##

- **Fixed:** dictionary.find_leaf_value. Infinite recursion for args: *key="a", dictionary={"a": "b", "b": "a"}*
- **Added:** New tests. Better coverage
- **Added:** text.are_anagram, text.fullstr.are_anagram
- **Added:** functional.once
- **Added:** iterator.centroid
- **Added:** Upgrade ruff and fix new warnings
- **Changed:** Remove fn useless iterator.contains, Improve performance of other "iterator.py" functions.

## v2.1.0 (2022-12-28) ##

- **Added:** Apply the *black* code formatter.
- **Added:** Apply ruff badge to README.
- **Added:** Install pre-commit. Run black, ruff, flake8 on pre-commit.
- **Added:** Apply pre-commit badge to README.
- **Added:** text.multireplace
- **Added:** algorithm.sieve_of_eratosthenes. *Primes less than n.*
- **Added:** functional.pipe. *Pipe function*
- **Improved:** iterator: splitter, uniques, uniquer, consume, all_equals, all_identical, all_equal, has_only_one

## v2.0.0 (2022-12-22) ##

- **Added:** Changelog
- **Added:** json.dump_from_csv
- **Added:** text.is_roman, text.fullstr('').is_roman
- **Fixed:** ruff warnings
