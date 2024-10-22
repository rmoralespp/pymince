import unittest.mock

import pytest

import pymince.functional


def test_retries_all_tries_when_condition_is_always_true():
    """Test that the function retries the maximum number of tries when the condition is always True."""

    func = unittest.mock.Mock()
    decorated_func = pymince.functional.retry_when(tries=3, condition=lambda x: True)(func)
    res = decorated_func()
    assert func.call_count == 3
    assert res is func.return_value


@pytest.mark.parametrize("tries", [0, -1])
def test_raises_error_on_negative_or_zero_tries(tries):
    """Test that the function raises a ValueError when the number of tries is zero or negative."""

    with pytest.raises(ValueError):
        pymince.functional.retry_when(tries=tries)


def test_does_not_retry_when_condition_is_false():
    """Test that the function does not retry when the condition evaluates to False."""

    func = unittest.mock.Mock()
    decorated_func = pymince.functional.retry_when(tries=3, condition=lambda x: False)(func)
    res = decorated_func()
    assert func.call_count == 1
    assert res is func.return_value
