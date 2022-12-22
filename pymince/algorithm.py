import itertools


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
    Returns a generator with fibonacci series.

    :param Optional[int] n: number iterations.
        Must be None or an integer: 0 <= x <= sys.maxsize
    :rtype: Generator[int]
    """

    def worker():
        a, b = 0, 1
        while True:
            yield a
            b = a + b
            yield b
            a = a + b

    it = worker()
    return itertools.islice(it, 0, n) if n is not None else it
