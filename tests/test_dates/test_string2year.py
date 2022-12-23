# -*- coding: utf-8 -*-
import pytest

import pymince.dates


def test_as_year_four_digits():
    assert pymince.dates.string2year("2053", shift=1953) == 2053


def test_as_year_two_digits_with_shift():
    assert pymince.dates.string2year("53") == 2053
    assert pymince.dates.string2year("53", shift=1953) == 1953
    assert pymince.dates.string2year("52", shift=1953) == 2052
    assert pymince.dates.string2year("54", shift=1953) == 1954
    assert pymince.dates.string2year("53", shift=1953, gte=1952, lte=1954) == 1953
    assert pymince.dates.string2year("53", shift=1953, gte=1953, lte=1953) == 1953


@pytest.mark.parametrize(
    "bad_year,gte,lte",
    [
        ("1", None, None),
        ("123", None, None),
        ("foo", None, None),
        ("12345", None, None),
        ("1995", 1996, None),
        ("1995", None, 1994),
        ("1995", 1996, 1994),
    ],
)
def test_as_year_with_errors(bad_year, gte, lte):
    with pytest.raises(ValueError):
        assert pymince.dates.string2year(bad_year, gte=gte, lte=lte)
