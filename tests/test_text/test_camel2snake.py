# -*- coding: utf-8 -*-

import pytest

import pymince.text


@pytest.mark.parametrize('value, expected', [
    ("", ""),
    ("snake_case", "snake_case"),
    ('camelCase', 'camel_case'),  # CamelCase
    ("CamelCase", "camel_case"),  # CamelCase
    ("ÑanDú", "ñan_dú"),  # Unicode
    ("UPPERCASE", "u_ppercase"),  # Uppercase
])
def test_camel2snake(value, expected):
    assert pymince.text.camel2snake(value) == expected
