import contextlib
import logging
import time


@contextlib.contextmanager
def timed_block(name):
    """
    Logger the duration of the handled context.

    Usage:
    >> logging.basicConfig(level=logging.DEBUG)
    >> with timed_block("sleeping"):
        >> time.sleep(1)

    INFO:root:Generating [sleeping]
    DEBUG:root:Finished [sleeping in 1.002 ms.]
    """
    logging.info('Generating [%s]', name)
    t0 = time.time()
    try:
        yield None
    finally:
        logging.debug('Finished [%s in %.3f ms.]', name, time.time() - t0)
