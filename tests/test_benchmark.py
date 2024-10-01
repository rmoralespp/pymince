# -*- coding: utf-8 -*-

import pytest

import pymince.benchmark as benchmark


@pytest.mark.parametrize("size,expected", [
    (0, (0, 'B')),
    (512, (512, 'B')),
    (1024, (1, 'KB')),
    (1025, (1.0009765625, 'KB')),
    (1024 ** 2, (1, 'MB')),
    (1024 ** 2.5, (32, 'MB')),
    (1024 ** 3, (1, 'GB')),
    (1024 ** 4, (1, 'TB')),
    (1024 ** 5, (1, 'PB')),
    (1024 ** 6, (1024, 'PB')),
])
def test_memoryUsage_human_readable_size(size, expected):
    assert benchmark.MemoryUsage().human_readable_size(size) == expected
