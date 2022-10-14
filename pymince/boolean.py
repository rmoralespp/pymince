def string2bool(value, ignorecase=False):
    """
    Function to convert a string representation of
    truth to True or False.

    :param str value: value to convert.
    :param bool ignorecase: Uppercase/lowercase letters of given "value" are ignored.

    :raise: "ValueError" if "value" is anything else.
    :rtype: bool

    Examples:
        from pymince.boolean import string2bool

        string2bool("true") # --> True
        string2bool("false") # --> False

        string2bool("TRUE") # --> ValueError
        string2bool("TRUE", ignorecase=True) # --> True

        string2bool("FALSE") # --> ValueError
        string2bool("FALSE", ignorecase=True) # --> False
    """

    checking = value.lower() if ignorecase else value
    if checking == 'true':
        return True
    elif checking == 'false':
        return False
    else:
        raise ValueError
