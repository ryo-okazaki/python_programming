import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG) # basicConfigよりも優先される

def do_something():
    logger.info('from logtest.py')
    logger.debug('debug')
    logger.warning('warning')
    logger.error('error')
    logger.critical('critical')