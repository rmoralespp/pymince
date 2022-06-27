import unittest.mock

import pytest

import pymince.iterator


@pytest.mark.parametrize('contained', (True, False))
def test_container(contained):
    obj = object()
    container = unittest.mock.Mock()
    container.__contains__ = unittest.mock.Mock(return_value=contained)
    result = pymince.iterator.contains(container, obj)
    container.__contains__.assert_called_once_with(obj)
    assert result is contained


@pytest.mark.parametrize('contained', (True, False))
def test_iterator(contained):
    search = "a"
    values = ("a", "b") if contained else ("b", "c")
    container = unittest.mock.Mock()
    container.__iter__ = lambda n: iter(values)
    result = pymince.iterator.contains(container, search)
    assert result is contained
