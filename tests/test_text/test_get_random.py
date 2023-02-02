# -*- coding: utf-8 -*-
import pytest

import pymince.text


@pytest.mark.parametrize("fn", (pymince.text.get_random_secret, pymince.text.get_random_string))
def test_get_random(fn):
    res = fn(10)
    assert isinstance(res, str)
    assert len(res) == 10
