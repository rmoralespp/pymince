# -*- coding: utf-8 -*-

import unittest.mock

import pymince.logging


def test_timed_block():
    logger = unittest.mock.Mock()
    with pymince.logging.timed_block("Testing", logger=logger):
        pass

    assert all((logger.info.called, logger.debug.called))
