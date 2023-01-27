# -*- coding: utf-8 -*-
import unittest.mock

import pymince.functional


def test_returns_none_with_tries():
    func = unittest.mock.Mock(return_value=None)
    decorated_func = pymince.functional.retry_if_none(tries=3)(func)
    res = decorated_func()
    assert func.call_count == 3
    assert res is func.return_value


def test_returns_none_without_tries():
    func = unittest.mock.Mock(return_value=None)
    decorated_func = pymince.functional.retry_if_none()(func)
    res = decorated_func()
    assert func.call_count == 1
    assert res is func.return_value


def test_returns_not_none():
    func = unittest.mock.Mock()
    decorated_func = pymince.functional.retry_if_none(tries=3)(func)
    res = decorated_func()
    assert func.call_count == 1
    assert res is func.return_value
