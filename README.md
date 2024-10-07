# pymince

[![CI](https://github.com/rmoralespp/pymince/workflows/CI/badge.svg)](https://github.com/rmoralespp/pymince/actions?query=event%3Arelease+workflow%3ACI)
[![pypi](https://img.shields.io/pypi/v/pymince.svg)](https://pypi.python.org/pypi/pymince)
[![versions](https://img.shields.io/pypi/pyversions/pymince.svg)](https://github.com/rmoralespp/pymince)
[![codecov](https://codecov.io/gh/rmoralespp/pymince/branch/main/graph/badge.svg)](https://app.codecov.io/gh/rmoralespp/pymince)
[![license](https://img.shields.io/github/license/rmoralespp/pymince.svg)](https://github.com/rmoralespp/pymince/blob/main/LICENSE)
[![Downloads](https://pepy.tech/badge/pymince)](https://pepy.tech/project/pymince)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Linter: ruff](https://img.shields.io/badge/linter-_ruff-orange)](https://github.com/charliermarsh/ruff)
[![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit)](https://github.com/pre-commit/pre-commit)

## About

**pymince** is a collection of useful tools that are "missing" from the Python standard library.

## Installation (via pip)

```pip install pymince```

## Documentation

See project [documentation](https://rmoralespp.github.io/pymince/) for more details.

## Development

### Build documentation

```
(env)$ pip install -r requirements-doc.txt   # Ignore this command if it has already been executed
(env)$ python upgrade-doc.py # Upgrade the documentation from the source code
(env)$ mkdocs serve # Start the live-reloading docs server
(env)$ mkdocs build # Build the documentation site
```

### Tests

```
(env)$ pip install -r requirements-dev.txt   # Ignore this command if it has already been executed
(env)$ pytest tests/
(env)$ pytest --cov pymince # Tests with coverge
```

## License

This project is licensed under the terms of the [MIT](LICENSE) license.
