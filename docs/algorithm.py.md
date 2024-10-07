# algorithm.py

##### fibonacci
```
fibonacci(n=None)

Returns a generator with fibonacci series up to n.
Runs indefinitely if n is specified as None.

:param Optional[int] n: Must be None or number.
:rtype: Generator[int]
```
##### luhn
```
luhn(value: str) -> bool

The Luhn algorithm or Luhn formula, also known as the "modulus 10" or "mod 10" algorithm,
named after its creator, IBM scientist Hans Peter Luhn,
is a simple checksum formula used to validate a variety of
identification numbers, such as credit card numbers, IMEI numbers, National Provider Identifier numbers

Based on: https://en.wikipedia.org/wiki/Luhn_algorithm
```
##### sieve_of_eratosthenes
```
sieve_of_eratosthenes(n)

Primes less than n.
Based on: https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes

:param int n: n an integer n > 1
:rtype: Generator[int]. All prime numbers from 2 through n.

Examples:
    from pymince.algorithm import sieve_of_eratosthenes as primes
    primes(30) # --> 2, 3, 5, 7, 11, 13, 17, 19, 23, 29
```