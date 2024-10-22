# -*- coding: utf-8 -*-

import unittest.mock

import pymince.benchmark


def test_timed():
    logger = unittest.mock.Mock()
    obj = pymince.benchmark.Timed("Testing", logger=logger, decimals=3)
    with obj:
        pass

    assert obj.decimals == 3
    assert logger.debug.called
