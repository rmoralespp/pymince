# -*- coding: utf-8 -*-
import operator

import pymince.functional


def test_call():
    caller = pymince.functional.caller(range(5))
    assert caller(len) == 5
    assert caller(list) == [0, 1, 2, 3, 4]


def test_call_with_multi_params():
    iterable, key = ((2,), (1,), (3,), (4,)), operator.itemgetter(0)
    caller = pymince.functional.caller(iterable, key=key)
    assert caller(sorted) == [(1,), (2,), (3,), (4,)]
