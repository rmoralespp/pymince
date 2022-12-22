import pymince.dictionary


def test_find_leaf_by_key():
    assert pymince.dictionary.find_leaf_value("a", {}) == "a"
    assert pymince.dictionary.find_leaf_value("a", {"a": "b"}) == "b"
    assert pymince.dictionary.find_leaf_value("a", {"a": "b", "b": "c"}) == "c"
    assert (
        pymince.dictionary.find_leaf_value("a", {"a": "b", "b": None, "c": "e"}) is None
    )
    assert pymince.dictionary.find_leaf_value("a", {"a": "a"}) == "a"
