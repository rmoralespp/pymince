import pytest

import utils.iterable


def test_consume():
    check = iter((1, 2, 3))
    utils.iterable.consume(check)
    with pytest.raises(StopIteration):
        next(check)
