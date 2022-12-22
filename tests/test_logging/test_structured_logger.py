import json
import logging
import sys

import pymince.json
import pymince.logging


def test_structured_formatter(capsys):
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
    logger.debug("", payload)
    # perform asserts
    captured = json.loads(capsys.readouterr().out)
    assert captured["payload"] == payload
    assert captured["level"] == "DEBUG"
