import contextlib
import logging
import time


@contextlib.contextmanager
def timed_block(name):
    logging.info('Generating [%s]', name)
    t0 = time.time()
    try:
        yield None
    finally:
        logging.debug('Finished [%s in %.3f ms.]', name, time.time() - t0)
