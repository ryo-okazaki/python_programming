import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG) # basicConfigよりも優先される

h = logging.FileHandler('logtest.log')
logger.addHandler(h) # ファイルに書き込まれるのはloggerだけ。
# loggingはコンソールに出力される
# lesson4で実行する


def do_something():
    logger.info('from logtest.py')
    logger.debug('debug')
    logger.warning('warning')
    logger.error('error')
    logger.critical('critical')