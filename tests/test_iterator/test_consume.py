import pytest

import utils.iterator


def test_consume():
    check = iter((1, 2, 3))
    utils.iterator.consume(check)
    with pytest.raises(StopIteration):
        next(check)
