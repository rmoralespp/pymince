def find_nested_key(key, dictionary):
    """
    Find key in dictionary.

    egg:
    * find_nested_key('a', {}) -> 'a'
    * find_nested_key('a', {'a': 'b', 'b': 'c'}) -> 'c'
    * find_nested_key('a', {'a': 'a'}) -> 'a'
    """
    while True:
        if key is not None and key in dictionary:
            new_key = dictionary[key]
            if new_key == key:
                break
            key = new_key
        else:
            break
    return key
