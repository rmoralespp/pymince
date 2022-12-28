# -*- coding: utf-8 -*-
import pytest

import pymince.algorithm


@pytest.mark.parametrize(
    "param, valid",
    [
        ("0", True),
        ("00", True),
        ("18", True),
        ("0000000000000000", True),
        ("4242424242424240", False),
        ("4242424242424241", False),
        ("4242424242424242", True),
        ("4242424242424243", False),
        ("4242424242424244", False),
        ("4242424242424245", False),
        ("4242424242424246", False),
        ("4242424242424247", False),
        ("4242424242424248", False),
        ("4242424242424249", False),
        ("42424242424242426", True),
        ("424242424242424267", True),
        ("4242424242424242675", True),
        ("5164581347216566", True),
        ("4345351087414150", True),
        ("343728738009846", True),
        ("5164581347216567", False),
        ("4345351087414151", False),
        ("343728738009847", False),
        ("000000018", True),
        ("99999999999999999999", True),
        ("99999999999999999999999999999999999999999999999999999999999999999997", True),
    ],
)
def test_luhn(param: str, valid: bool):
    # https://github.com/pydantic/pydantic/blob/a57346ac492273099389c564a482cbae7895a2ac/tests/test_types_payment_card_number.py#L40
    assert pymince.algorithm.luhn(param) == valid


def test_luhn_is_not_digit():
    assert not pymince.algorithm.luhn("foo123")
