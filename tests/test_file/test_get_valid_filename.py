# -*- coding: utf-8 -*-
import pytest

import pymince.file


def test_get_valid_filename():
    result = pymince.file.get_valid_filename(" ño bar-baz-$*?var ")
    assert result == "ño_bar-baz-var"


@pytest.mark.parametrize("bad", ("", ".", ".."))
def test_value_error(bad):
    with pytest.raises(ValueError):
        pymince.file.get_valid_filename(bad)
