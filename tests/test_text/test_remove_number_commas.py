import pytest

import utils.text


@pytest.mark.parametrize(
    "value,expected",
    [
        ('a', 'a'),
        ('1', '1'),
        ('1,2', '1,2',),
        ('1,23', '1,23'),
        ('a,bcd', 'a,bcd'),
        ('1,234', '1234',),
        ('1,234a', '1234a',),
        ('1,234,567', '1234567',),
        ('1,234,567.8', '1234567.8'),
    ],

)
def test_remove_number_commas(value, expected):
    result = utils.text.remove_number_commas(value)
    assert result == expected
