# -*- coding: utf-8 -*-

import pymince.iterator


def test_partition():
    left, right = pymince.iterator.partition(lambda x: x % 2 != 0, range(10))
    assert left == [0, 2, 4, 6, 8]
    assert right == [1, 3, 5, 7, 9]


def test_partition_all_left():
    left, right = pymince.iterator.partition(lambda x: x > 2 != 0, range(2))
    assert left == [0, 1]
    assert right == []


def test_partition_all_right():
    left, right = pymince.iterator.partition(lambda x: x < 2 != 0, range(2))
    assert left == []
    assert right == [0, 1]
