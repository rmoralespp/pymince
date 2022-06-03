import pytest

import pymince.iterator


def test_consume():
    check = iter((1, 2, 3))
    pymince.iterator.consume(check)
    with pytest.raises(StopIteration):
        next(check)
