import pytest

import utils.text


@pytest.mark.parametrize('ini_amount, end_amount_for', [
    ('2.1000000', ({'end_amount': '2.1'}, {'end_amount': '2.10', 'min_dec': 2})),
    ('2.0000000', ({'end_amount': '2'}, {'end_amount': '2.00', 'min_dec': 2})),
    ('2.000000', ({'end_amount': '2'}, {'end_amount': '2.00', 'min_dec': 2})),
    ('2.000100', ({'end_amount': '2.0001'}, {'end_amount': '2.0001', 'min_dec': 2})),
    ('2.1234000', ({'end_amount': '2.1234'}, {'end_amount': '2.1234', 'min_dec': 2})),
    ('0.0000000', ({'end_amount': '0'}, {'end_amount': '0', 'min_dec': 2})),
    ('2.', ({'end_amount': '2'}, {'end_amount': '2.00', 'min_dec': 2})),
    ('.323', ({'end_amount': '0.323'}, {'end_amount': '0.323', 'min_dec': 2})),
    ('', ({'end_amount': ''},)),
])
def test_remove_non_significant_decimal(ini_amount, end_amount_for):
    for case in end_amount_for:
        res = utils.text.remove_non_significant_decimal(ini_amount, min_decimals=case.get('min_dec'))
        assert res == case['end_amount']
