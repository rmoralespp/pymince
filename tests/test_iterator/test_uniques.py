import operator

import utils.iterable


def test_uniques_true():
    data = [
        {
            'id': 1,
            'name': 'n1',
        },
        {
            'id': 2,
            'name': 'n2',
        },
        {
            'id': 3,
            'name': 'n3',
        }
    ]
    uniques = utils.iterable.uniques(data, operator.itemgetter('id', 'name'))
    assert uniques


def test_uniques_false():
    data = [
        {
            'id': 1,
            'name': 'n1',
        },
        {
            'id': 1,
            'name': 'n1',
        },
        {
            'id': 3,
            'name': 'n3',
        }
    ]
    uniques = utils.iterable.uniques(data, operator.itemgetter('id', 'name'))
    assert not uniques
