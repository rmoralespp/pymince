import operator

import pytest

import utils.iterator


@pytest.mark.parametrize(
    "data,expected",
    [
        ((1, 1, 3), (1, 3)),
        ((1, 3, 1), (1, 3)),
    ],
)
def test_uniquer(data, expected):
    result = utils.iterator.uniquer(data)
    assert tuple(result) == expected


def test_uniquer_given_itemgetter():
    getter = operator.itemgetter("name")
    data = (
        {"id": 1, "name": "n1"},
        {"id": 2, "name": "n1"},
        {"id": 3, "name": "n2"}
    )
    result = utils.iterator.uniquer(data, getter=getter)
    assert tuple(result) == ({"id": 1, "name": "n1"}, {"id": 3, "name": "n2"})
