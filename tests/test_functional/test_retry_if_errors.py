# -*- coding: utf-8 -*-
import unittest.mock

import pytest

import pymince.functional


def test_catch_error_with_tries():
    func = unittest.mock.Mock(side_effect=ValueError)
    decorated_func = pymince.functional.retry_if_errors(ValueError, tries=3)(func)

    with pytest.raises(ValueError):
        decorated_func()
    assert func.call_count == 4


def test_catch_many_errors_with_tries():
    func = unittest.mock.Mock(side_effect=ValueError)
    decorated_func = pymince.functional.retry_if_errors(ValueError, TypeError, tries=3)(func)

    with pytest.raises(ValueError):
        decorated_func()
    assert func.call_count == 4


def test_catch_error_without_tries():
    func = unittest.mock.Mock(side_effect=ValueError)
    decorated_func = pymince.functional.retry_if_errors(ValueError)(func)

    with pytest.raises(ValueError):
        decorated_func()
    assert func.call_count == 2


def test_not_raise_error():
    func = unittest.mock.Mock()
    decorated_func = pymince.functional.retry_if_errors(ValueError, tries=3)(func)
    res = decorated_func()
    assert func.call_count == 1
    assert res is func.return_value


def test_catch_other_error():
    func = unittest.mock.Mock(side_effect=TypeError)
    decorated_func = pymince.functional.retry_if_errors(ValueError, tries=3)(func)

    with pytest.raises(TypeError):
        decorated_func()
    assert func.call_count == 1


def test_not_catch_error():
    func = unittest.mock.Mock(side_effect=ValueError)
    decorated_func = pymince.functional.retry_if_errors(tries=3)(func)

    with pytest.raises(ValueError):
        decorated_func()
    assert func.call_count == 1
