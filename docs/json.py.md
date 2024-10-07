# json.py
Useful functions for working with JSONs.
- Supports `orjson`, `ujson` libraries or standard `json`.
- Supports following compression formats: gzip => (.gz), bzip2 => (.bz2), xz => (.xz)
##### JSONEncoder
```
JSONEncoder(*, skipkeys=False, ensure_ascii=True, check_circular=True, allow_nan=True, sort_keys=False, indent=None, separators=None, default=None)

JSON encoder that handles additional types compared
to `json.JSONEncoder`

- `datetime` and `date` are serialized to strings according to the isoformat.
- `decimal.Decimal` is serialized to a string.
- `uuid.UUID` is serialized to a string.
- `dataclasses.dataclass` is passed to `dataclasses.asdict`.
- `frozenset` and `set` are serialized by ordering their values.
```
##### dump_from_csv
```
dump_from_csv(csv_path, json_path, /, *, fieldnames=None, start=0, stop=None, strip=True, encoding='utf-8', **kwargs)

Dump CSV file to a JSON file.
- Use (`.gz`, `.xz`, `.bz2`) extensions to create a compressed file.
- Dumps falls back to the functions: (`orjson.dumps`, `ujson.dumps`, and `json.dumps`).

:param str csv_path:
:param str json_path:
:param fieldnames: list of keys for the JSON
:param int start:
    If start is specified, will skip all preceding elements;
    otherwise, start defaults to zero.
:param int stop:
:param bool strip:
    Whether white space should be removed from the
    beginning and end of field values.
:param str encoding: utf-8 is used by default.
```
##### dump_into
```
dump_into(filename, obj, encoding='utf-8', **kwargs)

Dump JSON to a file.
- Use (`.gz`, `.xz`, `.bz2`) extensions to create compressed files.
- Dumps falls back to the functions: (`orjson.dump`, `ujson.dump`, and `json.dump`).

Examples:
    from pymince.json import dump_into

    dump_into("foo.json", {"key": "value"})     # uncompressed
    dump_into("foo.json.gz", {"key": "value"})  # gzip-compressed
    dump_into("foo.json.xz", {"key": "value"})  # lzma-compressed
    dump_into("foo.json.bz2", {"key": "value"}) # bz2-compressed
```
##### dump_into_zip
```
dump_into_zip(zip_path, arcname, payload, **kwargs)

Dump JSON into the zip archive under the name arcname.

Examples:
    from pymince.json import dump_into_zip

    dump_into_zip("archive.zip", "foo.json", {"key": "value"})
```
##### idump_fork
```
idump_fork(path_items, encoding='utf-8', dump_if_empty=True, **dumps_kwargs)

Incrementally dumps different groups of elements into
the indicated JSON file.
*** Useful to reduce memory consumption ***

- Use (`.gz`, `.xz`, `.bz2`) extensions to create compressed files.
- Dumps falls back to the functions: (`orjson.dumps`, `ujson.dumps`, and `json.dumps`).

:param Iterable[file_path, Iterable[dict]] path_items: group items by file path
:param encoding: 'utf-8' by default.
:param bool dump_if_empty: If false, don't create an empty file.
:param dumps_kwargs: json.dumps kwargs.

Examples:
    from pymince.json import idump_fork

    path_items = (
        ("num.json.gz", ({"value": 1}, {"value": 2})),
        ("num.json.gz", ({"value": 3},)),
        ("foo.json", ({"a": "1"}, {"b": 2})),
        ("baz.json", ()),
    )
    idump_fork(iter(path_items))
```
##### idump_into
```
idump_into(filename, iterable, encoding='utf-8', **kwargs)

Dump an iterable incrementally into a JSON file.
- Use (`.gz`, `.xz`, `.bz2`) extensions to create compressed files.
- Dumps falls back to the functions: (`orjson.dumps`, `ujson.dumps`, and `json.dumps`).

The result will always be an array with the elements of the iterable.
*** Useful to reduce memory consumption ***

Examples:
    from pymince.json import idump_into

    values = ([{"key": "foo"}, {"key": "bar"}])

    idump_into("foo.json", values)     # uncompressed
    idump_into("foo.json.gz", values)  # gzip-compressed
    idump_into("foo.json.xz", values)  # lzma-compressed
    idump_into("foo.json.bz2", values) # bz2-compressed
```
##### idump_lines
```
idump_lines(iterable, **dumps_kwargs)

Generator yielding string lines that form a JSON array
with the serialized elements of given iterable.
*** Useful to reduce memory consumption ***
- Dumps falls back to the functions: (`orjson.dumps`, `ujson.dumps`, and `json.dumps`).

:param iterable: Iterable[dict]
:rtype: Iterable[str]
```
##### load
```
load(fp, *, cls=None, object_hook=None, parse_float=None, parse_int=None, parse_constant=None, object_pairs_hook=None, **kw)

Deserialize ``fp`` (a ``.read()``-supporting file-like object containing
a JSON document) to a Python object.

``object_hook`` is an optional function that will be called with the
result of any object literal decode (a ``dict``). The return value of
``object_hook`` will be used instead of the ``dict``. This feature
can be used to implement custom decoders (e.g. JSON-RPC class hinting).

``object_pairs_hook`` is an optional function that will be called with the
result of any object literal decoded with an ordered list of pairs.  The
return value of ``object_pairs_hook`` will be used instead of the ``dict``.
This feature can be used to implement custom decoders.  If ``object_hook``
is also defined, the ``object_pairs_hook`` takes priority.

To use a custom ``JSONDecoder`` subclass, specify it with the ``cls``
kwarg; otherwise ``JSONDecoder`` is used.
```
##### load_from
```
load_from(filename, encoding='utf-8')

Load JSON from a file.
- Recognizes (`.gz`, `.xz`, `.bz2`) extensions to load compressed files.
- Loads falls back to the functions: (`orjson.load`, `ujson.load`, and `json.load`).

Examples:
    from pymince.json import load_from

    dictionary1 = load_from("foo.json")     # uncompressed
    dictionary2 = load_from("foo.json.gz")  # gzip-compressed
    dictionary3 = load_from("foo.json.xz")  # lzma-compressed
    dictionary4 = load_from("foo.json.bz2") # bz2-compressed
```
##### load_from_zip
```
load_from_zip(zip_path, arcname)

Load JSON from a file named "arcname" inside a zip archive.

Examples:
    from pymince.json import load_from_zip

    dictionary = load_from_zip("archive.zip", "foo.json")
```