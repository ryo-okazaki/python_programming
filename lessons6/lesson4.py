"""
CRITICAL
ERROR
WARNING
INFO
DEBUG
"""

import logging

from lessons6 import logtest

logging.basicConfig(level=logging.INFO)

class NoPassFilter(logging.Filter):
    def filter(self, record):
        log_message = record.getMessage()
        return 'password' not in log_message

logger = logging.getLogger(__name__)
logger.addFilter(NoPassFilter())
logger.debug('debug')
logger.debug('debug passsword = "test"')

logtest.do_something()

# メイン関数ではロギングを設定する
# そのあとはloggerを使う