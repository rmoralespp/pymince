import pymince.dictionary


def test_key_or_leaf_value():
    assert pymince.dictionary.key_or_leaf_value('a', {}) == 'a'
    assert pymince.dictionary.key_or_leaf_value('a', {'a': 'b'}) == 'b'
    assert pymince.dictionary.key_or_leaf_value('a', {'a': 'b', 'b': 'c'}) == 'c'
    assert pymince.dictionary.key_or_leaf_value('a', {'a': 'b', 'b': None, 'c': 'e'}) is None
    assert pymince.dictionary.key_or_leaf_value('a', {'a': 'a'}) == 'a'
