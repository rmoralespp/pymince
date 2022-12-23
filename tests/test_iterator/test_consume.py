# -*- coding: utf-8 -*-
import pytest

import pymince.iterator


def test_consume_entirely():
    check = iter((1, 2, 3))
    pymince.iterator.consume(check)
    with pytest.raises(StopIteration):
        next(check)


def test_consume_partially():
    check = iter((1, 2, 3))
    pymince.iterator.consume(check, n=2)
    assert next(check) == 3


def test_consume_entirely_with_n():
    check = iter((1, 2))
    pymince.iterator.consume(check, n=2)
    with pytest.raises(StopIteration):
        next(check)
