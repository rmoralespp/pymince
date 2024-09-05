# -*- coding: utf-8 -*-
import pytest

import pymince.algorithm


@pytest.mark.parametrize('v', (0, 1, 2))
def test_returns_empty(v):
    res = pymince.algorithm.sieve_of_eratosthenes(v)
    assert tuple(res) == ()


def test_value_error():
    with pytest.raises(ValueError):
        tuple(pymince.algorithm.sieve_of_eratosthenes(-1))


@pytest.mark.parametrize('v', (100, 99, 98))
def test_returns_primes_1_100(v):
    expected = (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97)
    res = pymince.algorithm.sieve_of_eratosthenes(v)
    assert tuple(res) == expected
