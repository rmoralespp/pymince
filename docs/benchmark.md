# Benchmark
Benchmarking utilities.

**MemoryUsage**
```
MemoryUsage(name=None, logger=None)

Usage:

import logging
import pymince.benchmark as benchmark

logging.basicConfig(level=logging.DEBUG)

# Using context manager
with benchmark.MemoryUsage():
    print(sum(list(range(1000))))

# Using decorator
@benchmark.MemoryUsage()
def calculate():
    print(sum(list(range(1000))))
calculate()
```
**Timed**
```
Timed(name=None, logger=None, decimals=3)

Usage:

import logging
import pymince.benchmark as benchmark

logging.basicConfig(level=logging.DEBUG)

# Using context manager
with benchmark.Timed():
    print(sum(list(range(1000))))

# Using decorator
@benchmark.Timed()
def calculate():
    print(sum(list(range(1000))))
calculate()
```