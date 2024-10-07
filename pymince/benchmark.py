# -*- coding: utf-8 -*-

"""Benchmarking utilities."""

import functools
import logging
import time
import tracemalloc


class _Benchmark:

    def __init__(self, name=None, logger=None):
        self.name = name or self.__class__.__name__
        self.logger = logger or logging

    def __call__(self, fn):
        @functools.wraps(fn)
        def decorator(*args, **kwargs):
            # Avoid it replace the original name on decorator.
            fn_name = getattr(fn, "__name__", self.name)
            with self.__class__(name=fn_name, logger=self.logger):
                return fn(*args, **kwargs)

        return decorator


class Timed(_Benchmark):
    """
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

    def trace(self, mark):
        current, peak = tracemalloc.get_traced_memory()
        current, unit_current = self.human_readable_size(current)
        peak, unit_peak = self.human_readable_size(peak)

        info = "%s - %s: [Current RAM usage: %.1f %s; Peak: %.1f %s]"
        self.logger.debug(info, self.name, mark, current, unit_current, peak, unit_peak)

    @staticmethod
    def human_readable_size(bytes_numb):
        """Convert bytes into a human-readable format."""

        for unit in ("B", "KB", "MB", "GB", "TB"):
            if bytes_numb < 1024:
                return (bytes_numb, unit)
            else:
                bytes_numb /= 1024
        return (bytes_numb, "PB")
