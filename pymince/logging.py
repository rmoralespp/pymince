# -*- coding: utf-8 -*-

"""Logging utilities."""

import json
import logging


class StructuredFormatter(logging.Formatter):
    """
    Implementation of JSON structured logging that works
    for most handlers.

    Examples:
        import logging
        import sys
        from pymince.logging import StructuredFormatter

        # Config
        logger = logging.getLogger()
        logger.setLevel(logging.DEBUG)
        formatter = StructuredFormatter('%(message)s')
        handler = logging.StreamHandler(sys.stdout)
        handler.setLevel(logging.DEBUG)
        handler.setFormatter(formatter)
        logger.addHandler(handler)

        # Usage
        logger.debug('', {"string": "value1", "number": 1})
        logger.debug('', {"string": "value2", "number": 2})

        >>Output<<
        {"timestamp":"2022-06-17 18:37:48,789","level":"DEBUG","payload":{"string":"value1","number":1}}
        {"timestamp":"2022-06-17 18:37:48,789","level":"DEBUG","payload":{"string":"value2","number":2}}
    """

    json_dumper = json.JSONEncoder(separators=(",", ":")).encode  # Most compact form

    def format(self, record: logging.LogRecord) -> str:
        """
        Overrides parent format function.

        :param record: logging.LogRecord object
        :return: JSON string
        """

        payload = self.make_structured_dict(record)
        return self.json_dumper(payload)

    def make_structured_dict(self, record: logging.LogRecord) -> dict:
        """
        Create the dictionary that requires (json_dumper).

        :param record: logging.LogRecord object
        :return: dict
        """

        if not isinstance(record.args, dict):
            raise TypeError("Invalid logger arguments.")

        return {
            "timestamp": self.formatTime(record, self.datefmt),
            "level": record.levelname,
            "payload": record.args,
        }


class ColoredFormatter(logging.Formatter):
    """
    A class for formatting colored logs.

    Default colors:
    - DEBUG: blue
    - INFO: green
    - WARNING: yellow
    - ERROR: red
    - CRITICAL: red

    Examples:
        import logging
        from pymince.logging import ColoredFormatter

        # Config
        logger = logging.getLogger('mylog')
        logger.setLevel('DEBUG')

        stream_handler = logging.StreamHandler()
        stream_handler.setFormatter(ColoredFormatter(logging.BASIC_FORMAT))
        logger.addHandler(stream_handler)

        # Use default colors
        logger.debug("This is debug") # blue color

        # Use custom colors
        import colorama

        black = colorama.Fore.BLACK
        bold_black_on_green = colorama.Back.GREEN + colorama.Fore.BLACK + colorama.Style.BRIGHT
        bold_green_on_black = colorama.Back.BLACK + colorama.Fore.GREEN + colorama.Style.BRIGHT

        logger.debug("This is debug", extra={"color": black})
        logger.debug("This is debug", extra={"color": bold_black_on_green})
        logger.debug("This is debug", extra={"color": bold_green_on_black})
    """

    COLORS = {
        logging.DEBUG: "\033[94m",  # blue
        logging.INFO: "\033[92m",  # green
        logging.WARNING: "\033[93m",  # yellow
        logging.ERROR: "\033[91m",  # red
        logging.CRITICAL: "\033[1;31m",  # bold red
    }

    def format(self, record):
        formatted = super().format(record)
        if hasattr(record, "color"):
            color = record.color
        else:
            level = logging._nameToLevel[record.levelname]
            color = self.COLORS[level]
        return f"{color}{formatted}\033[0m"


class ColoredLogger:
    """
    Custom logger to generate color logs.

    Examples:
        from pymince.logging import ColoredLogger

        logger = ColoredLogger()

        # Use default colors
        logger.debug("This is debug") # blue color

        # Use custom colors
        import colorama
        logger.debug("This is debug", extra={"color": colorama.Fore.BLACK})
    """

    def __init__(self, name=None, level=logging.DEBUG, **fmt_kwargs):
        self.logger = logging.getLogger(name or __name__)
        self.logger.setLevel(level)

        stream_handler = logging.StreamHandler()
        stream_handler.setFormatter(ColoredFormatter(**fmt_kwargs))
        self.logger.addHandler(stream_handler)

    def __getattr__(self, item):
        return getattr(self.logger, item)
