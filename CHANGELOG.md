## Releases ##

## v2.13.0 (2025-03-19) ##

- **Added:** `patterns.Singleton` Metaclass to create singletons.
- **Added:** `text.camel2snake` Utility to convert camel case to snake case.
- **Changed:** The default `stop_date` param for `dates.irange` is now `datetime.now()` (naive) if not provided.
- **Changed:** `iterator.grouper` now uses `itertools.batched` internally if a Python version is 3.12 or higher.
- **Changed:** Update `pyproject.toml`

## v2.12.0 (2024-10-22) ##

- **Added:** Generate documentation site with `mkdocs`.
- **Changed:** Simplify the README.
- **Changed:** [BREAKING] Remove `logging.timed_block`. Use instead `benchmark.Timed`.
- **Changed:** [BREAKING] Rename `functional.retry_if_none` to `functional.retry_when`. Now retries based on the given
  condition, By default, it retries if the result is None.
- **Changed:** [BREAKING] `functional.retry_if_errors` avoid additionally retrying, raise ValueError.
- **Changed:** [BREAKING] Remove `orjson`, `ujson` libraries supports. Use instead `json` module.
- **Changed:** [BREAKING] Rename `json.dump_from_csv` to `json.csv_to_json`.

## v2.11.4 (2024-10-01) ##

- **Fixed:** Fix "benchmark" decorators. Humanize size memory consumption.

## v2.11.3 (2024-10-01) ##

- **Added:** Improve "benchmark" decorators to avoid replacing given aliases. Improvement to
  remove '_Benchmark' class from README.md

## v2.11.2 (2024-10-01) ##

- **Added:** `benchmark`: Utilities to measure memory consumption and duration of a given code fragment.

## v2.11.1 (2024-09-05) ##

- **Changed:** `text.is_positive_int`, `text.is_negative_int`, `text.is_int`. Now it is stricter
- **Changed:** `json` module. Supports `orjson`, `ujson` libraries or standard `json`. Supports following compression
  formats: gzip => (.gz), bzip2 => (.bz2), xz => (.xz)
- **Changed:** `file.decompress`: Supports more compression formats: gzip => (.gz), bzip2 => (.bz2), xz => (.xz)

## v2.10.1 (2024-09-05) ##

- **Added:** `logging.ColoredFormatter`, `logging.ColoredLogger`: Generates colored logs.
- **Added:** `text.slugify`: Generate slug from string.
- **Changed:** `functional.classproperty`: Descriptor to change the getter on a classproperty.
- **Changed:** Remove `jsonlines` module. Use instead "https://github.com/rmoralespp/jsonl" package.

## v2.9.0 (2023-06-23) ##

- **Added:** `jsonlines.dump_fork`: Incrementally dumps different groups of elements
  into the indicated `jsonlines` file.
- **Added:** tests to `json.idump_fork`
- **Added:** `json.idump_fork`: Incrementally dumps different groups of elements into
  the indicated JSON file. *** Useful to reduce memory consumption ***

## v2.8.0 (2023-06-16) ##

- **Added:** `dictionary.tree`
- **Added:** new tests to `logging` `iterator`
- **Added:** new tests to `jsonlines`
- **Added:** `jsonlines module:` Useful functions for working with `jsonlines` and `ndjson`:
  dumper, dumps, dump, dump_into, load, load_from.
  TODO: stream compressors: `gzip` `bzip2` supporting

## v2.7.0 (2023-05-11) ##

- **Improved:** `json.dump_from_csv` reduce memory consumption, now uses `idump_into`
- **Added:** `json.idump_lines`

## v2.6.0 (2023-04-17) ##

- **Added:** `json.idump_into`
- **Added:** `file.get_valid_filename`
- **Added:** `iterator.partition`
- **Added:** `iterator.normalize_newlines`
- **Changed:** Rename `iterator.has_only_one` to `iterator.only_one`

## v2.5.0 (2023-02-17) ##

- **Fixed:** `logging.timed_block` docstring
- **Added:** `text.get_random_secret`, `text.get_random_string`
- **Added:** `functional.identity` Identity function, as defined in *https://en.wikipedia.org/wiki/Identity_function*.
- **Added:** `text.multireplacer` Returns a multiple replacement function.
- **Added:** `iterator.ipush` Iterator class supporting **append** and **prepend**.
- **Added:** `dates.IsoWeekDay`, `dates.WeekDay` enums.

## v2.4.0 (2023-01-30) ##

- **Fixed** `text.multireplace`
- **Added:** `functional.caller`, `functional.suppress`
- **Changed:** Moved `retry.retry_if_errors`, `retry.retry_if_none` to
  `functional.retry_if_errors`, `functional.retry_if_none`
- **Changed:** `retry.retry_if_errors`. Used `functools.wraps` to apply **update_wrapper**.
- **Changed:** `file.decompress`. Added `size` arg.
- **Changed:** Purpose of **n** arg of `algorithm.fibonacci`.
- **Changed:** `json.dump_into`, `json.dump_into_zip`, `json.dump_from_csv`. Pass `**kwargs` to **json.dump/s**

## v2.3.0 (2023-01-13) ##

- **Added:** `iterator.mul`, `iterator.truediv`, `iterator.sub`
- **Added:** `functional.set_attributes`
- **Added:** `json.JSONEncoder`. Handles additional types compared to `json.JSONEncoder`
- **Changed:** `dictionary.DigestGetter`. Now does not support enums and uses the new `pymince.json.JSONEncoder`.

## v2.2.1 (2023-01-12) ##

- **Fixed:** README

## v2.2.0 (2023-01-12) ##

- **Fixed:** `dictionary.find_leaf_value`. Infinite recursion for args: `key="a", dictionary={"a": "b", "b": "a"}`
- **Added:** New tests. Better coverage
- **Added:** `text.are_anagram`, `text.fullstr.are_anagram`
- **Added:** `unctional.once`
- **Added:** `iterator.centroid`
- **Added:** Upgrade ruff and fix new warnings
- **Changed:** Remove fn useless `iterator.contains`. Improve performance of other `iterator.py` functions.

## v2.1.0 (2022-12-28) ##

- **Added:** Apply the *black* code formatter.
- **Added:** Apply ruff badge to README.
- **Added:** Install pre-commit. Run black, ruff, flake8 on pre-commit.
- **Added:** Apply pre-commit badge to README.
- **Added:** `text.multireplace`
- **Added:** `algorithm.sieve_of_eratosthenes`. *Primes less than n.*
- **Added:** `functional.pipe`. *Pipe function*
- **Improved:** iterator: `splitter`, `uniques`, `uniquer`, `consume`, `all_equals`, `all_identical`, `all_equal`,
  `has_only_one`

## v2.0.0 (2022-12-22) ##

- **Added:** Changelog
- **Added:** `json.dump_from_csv`
- **Added:** `text.is_roman`, `text.fullstr('').is_roman`
- **Fixed:** ruff warnings
