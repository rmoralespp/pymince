# -*- coding: utf-8 -*-

import pymince.functional


def test_call():
    x = object()
    assert pymince.functional.identity(x) is x
