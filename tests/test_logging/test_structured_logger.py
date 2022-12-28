# -*- coding: utf-8 -*-
import json
import logging
import sys

import pytest

import pymince.json
import pymince.logging


def get_logger():
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)
    formatter = pymince.logging.StructuredFormatter("%(message)s")
    handler = logging.StreamHandler(sys.stdout)
    handler.setLevel(logging.DEBUG)
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    return logger


def test_structured_formatter(capsys):
    # prepare logging
    logger = get_logger()
    payload = {"key": "a", "numb": 1, "bool": True, "nested": [1, 2, 3]}
    # execute log.debug
    logger.debug("", payload)
    # perform asserts
    captured = json.loads(capsys.readouterr().out)
    assert captured["payload"] == payload
    assert captured["level"] == "DEBUG"


def test_invalid_payload():
    # prepare logging
    logger = get_logger()
    with pytest.raises(TypeError):
        logger.debug("", object())
