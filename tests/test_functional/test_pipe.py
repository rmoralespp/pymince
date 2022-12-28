# -*- coding: utf-8 -*-
import pytest

import pymince.functional


def test_pipe():
    def addtwo(n):
        return n + 2

    def double(n):
        return n * 2

    def square(n):
        return n * n

    fn = pymince.functional.pipe(addtwo, double, square)
    assert fn(1) == 36


def test_empty():
    expected = v = 1
    fn = pymince.functional.pipe()
    assert fn(v) == expected


def test_missing_arguments():
    def square(n, m):
        return n * m

    with pytest.raises(TypeError):
        fn = pymince.functional.pipe(square)
        fn(1)


def test_unexpected_arguments():
    def square(n):
        return n * n

    with pytest.raises(TypeError):
        fn = pymince.functional.pipe(square)
        fn(1, 2)
