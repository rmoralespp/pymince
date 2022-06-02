import utils.dictionary


def test_key_or_leaf_value():
    assert utils.dictionary.key_or_leaf_value('a', {}) == 'a'
    assert utils.dictionary.key_or_leaf_value('a', {'a': 'b'}) == 'b'
    assert utils.dictionary.key_or_leaf_value('a', {'a': 'b', 'b': 'c'}) == 'c'
    assert utils.dictionary.key_or_leaf_value('a', {'a': 'b', 'b': None, 'c': 'e'}) is None
    assert utils.dictionary.key_or_leaf_value('a', {'a': 'a'}) == 'a'
