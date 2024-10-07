# -*- coding: utf-8 -*-

"""Contains useful algorithms."""

import math


def luhn(value: str) -> bool:
    """
    The Luhn algorithm or Luhn formula, also known as the "modulus 10" or "mod 10" algorithm,
    named after its creator, IBM scientist Hans Peter Luhn,
    is a simple checksum formula used to validate a variety of
    identification numbers, such as credit card numbers, IMEI numbers, National Provider Identifier numbers

    Based on: https://en.wikipedia.org/wiki/Luhn_algorithm
    """

    if not value.isdigit():
        return False

    sum_total = int(value[-1])
    length = len(value)
    parity = length % 2
    for i in range(length - 1):
        digit = int(value[i])
        if i % 2 == parity:
            digit *= 2
        if digit > 9:
            digit -= 9
        sum_total += digit

    return sum_total % 10 == 0


def fibonacci(n=None):
    """
    Returns a generator with fibonacci series up to n.
    Runs indefinitely if n is specified as None.

    :param Optional[int] n: Must be None or number.
    :rtype: Generator[int]
    """

    a, b = 0, 1
    while n is None or a < n:
        yield a
        a, b = b, a + b


def sieve_of_eratosthenes(n):
    """
    Primes less than n.
    Based on: https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes

    :param int n: n an integer n > 1
    :rtype: Generator[int]. All prime numbers from 2 through n.

    Examples:
        from pymince.algorithm import sieve_of_eratosthenes as primes
        primes(30) # --> 2, 3, 5, 7, 11, 13, 17, 19, 23, 29
    """

    sieve = bytearray((0, 0)) + bytearray((1,)) * (n - 2)
    limit = int(math.sqrt(n) + 1)
    for p in range(2, limit):
        if sieve[p]:
            mulp = p * p
            size = len(range(mulp, n, p))
            sieve[mulp:n:p] = bytes(size)
    prime = (i for i, v in enumerate(sieve) if v)
    yield from prime
