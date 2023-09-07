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

logging.info('info')

logger = logging.getLogger(__name__)
logger.debug('debug')

logtest.do_something()

# メイン関数ではロギングを設定する
# そのあとはloggerを使う