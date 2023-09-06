"""
CRITICAL
ERROR
WARNING
INFO
DEBUG
"""
import logging

# formatter = '%(levelname)s%:%(message)s'
formatter = '%(asctime)s%:%(message)s'
logging.basicConfig(filename='test.log', level=logging.INFO)
# ログのレベルを変える

logging.critical('critical')
logging.error('error')
logging.warning('warning')
logging.info('info')
logging.debug('debug')

logging.info('info {}'.format('test'))
logging.info('info %s %s' % ('test', 'test2'))
logging.info('info %s %s', 'test', 'test2')