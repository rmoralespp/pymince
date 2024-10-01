# -*- coding: utf-8 -*-

import functools
import logging
import time
import tracemalloc


class _Benchmark:

    def __init__(self, name=None, logger=None):
        self.name = name or self.__class__.__name__
        self.logger = logger or logging

    def __call__(self, fn):
        name = getattr(fn, "__name__", self.name)

        @functools.wraps(fn)
        def decorator(*args, **kwargs):
            with _Benchmark(name=name, logger=self.logger):
                return fn(*args, **kwargs)

        return decorator


class Timed(_Benchmark):
    """
    Usage:

    logging.basicConfig(level=logging.DEBUG)

    # Using context manager
    with Timed():
        print(sum(list(range(1000))))

    # Using decorator
    @Timed()
    def calculate():
        print(sum(list(range(1000))))
    calculate()
    """

    def __init__(self, name=None, logger=None, decimals=3):
        super().__init__(name=name, logger=logger)
        self.decimals = decimals

    def __enter__(self):
        self.start_time = time.perf_counter()

    def __exit__(self, *args, **kwargs):
        self.end_time = time.perf_counter()
        elapsed_time = self.end_time - self.start_time
        self.logger.debug(f"{self.name}: [{elapsed_time:.{self.decimals}f} seconds]")


class MemoryUsage(_Benchmark):
    """
    Usage:

    logging.basicConfig(level=logging.DEBUG)

    # Using context manager
    with MemoryUsage():
        print(sum(list(range(1000))))

    # Using decorator
    @MemoryUsage()
    def calculate():
        print(sum(list(range(1000))))
    calculate()
    """

    def __enter__(self):
        if not tracemalloc.is_tracing():
            tracemalloc.start()
        tracemalloc.reset_peak()
        self.trace("starting")

    def __exit__(self, *args, **kwargs):
        self.trace("finished")
        if tracemalloc.is_tracing():
            tracemalloc.stop()

    def trace(self, when):
        this, peak = tracemalloc.get_traced_memory()
        info = "%s - %s: [Current RAM usage: %.1f KB; Peak: %.1f} KB]"
        self.logger.debug(info, self.name, when, this / 1024, peak / 1024)
