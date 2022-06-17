import pytest

import pymince.text


def test_string2bool_true():
    assert pymince.text.string2bool("true") is True


def test_string2bool_true_with_ignorecase():
    assert pymince.text.string2bool("TRUE", ignorecase=True) is True


def test_string2bool_true_with_error():
    with pytest.raises(ValueError):
        assert pymince.text.string2bool("TRUE", ignorecase=False)


def test_string2bool_false():
    assert pymince.text.string2bool("false") is False


def test_string2bool_false_with_ignorecase():
    assert pymince.text.string2bool("FALSE", ignorecase=True) is False


def test_string2bool_false_with_error():
    with pytest.raises(ValueError):
        assert pymince.text.string2bool("FALSE", ignorecase=False)
