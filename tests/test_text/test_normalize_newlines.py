# -*- coding: utf-8 -*-

import pymince.text


def test_normalize_newlines():
    s = "abc\ndefg\r\nght\rjk"
    result = pymince.text.normalize_newlines(s)
    assert result == "abc\ndefg\nght\njk"
