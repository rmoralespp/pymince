# Logging
Logging utilities.

**ColoredFormatter**
```
ColoredFormatter(fmt=None, datefmt=None, style='%', validate=True, *, defaults=None)

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
```
**ColoredLogger**
```
ColoredLogger(name=None, level=10, **fmt_kwargs)

Custom logger to generate color logs.

Examples:
    from pymince.logging import ColoredLogger

    logger = ColoredLogger()

    # Use default colors
    logger.debug("This is debug") # blue color

    # Use custom colors
    import colorama
    logger.debug("This is debug", extra={"color": colorama.Fore.BLACK})
```
**StructuredFormatter**
```
StructuredFormatter(fmt=None, datefmt=None, style='%', validate=True, *, defaults=None)

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
```