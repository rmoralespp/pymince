# -*- coding: utf-8 -*-

import json
import logging
import sys
import unittest.mock

import pymince.json
import pymince.logging


@unittest.mock.patch('logging.StreamHandler.handleError')
def test_structured_formatter(mock_handle_error, capsys):
    # prepare logging
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)
    formatter = pymince.logging.StructuredFormatter("%(message)s")
    handler = logging.StreamHandler(sys.stdout)
    handler.setLevel(logging.DEBUG)
    handler.setFormatter(formatter)
    logger.addHandler(handler)

    payload = {"key": "a", "numb": 1, "bool": True, "nested": [1, 2, 3]}
    # execute log.debug
    logger.debug("", payload)  # noqa: PLE1205
    # perform asserts
    captured = json.loads(capsys.readouterr().out)
    assert captured["payload"] == payload
    assert captured["level"] == "DEBUG"
    mock_handle_error.assert_not_called()

    # check TypeError
    logger.debug("foo")
    mock_handle_error.assert_called_once()
