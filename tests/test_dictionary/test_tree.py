# -*- coding: utf-8 -*-

import pymince.dictionary


def test_empty():
    assert pymince.dictionary.tree() == {}


def test_no_empty():
    tree = pymince.dictionary.tree()
    tree['harold']['username'] = 'hrldcpr'
    assert tree == {"harold": {"username": 'hrldcpr'}}
