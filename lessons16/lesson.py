from multiprocessing import (
    Process,
    Lock, RLock, Semaphore, Queue, Event, Condition, Barrier, # スレッド
    Value, Array, Pipe, Manager
)
"""
マルチスレッド
import logging
import threading
import time

logging.basicConfig(level=logging.DEBUG, format='%(threadName)s: %(message)s')

def worker1(i):
    logging.debug('start')
    logging.debug(i)
    logging.debug('end')

def worker2(i):
    logging.debug('start')
    logging.debug(i)
    logging.debug('end')

if __name__ == '__main__':
    i = 10
    t1 = threading.Thread(target=worker1, args=(i,))
    t2 = threading.Thread(name='renamed worker2', target=worker2, args=(i,))
    t1.start()
    t2.start()
"""

import logging
import multiprocessing
import time

logging.basicConfig(level=logging.DEBUG, format='%(processName)s: %(message)s')

def worker1(i):
    logging.debug('start')
    logging.debug(i)
    time.sleep(5)
    logging.debug('end')

def worker2(i):
    logging.debug('start')
    logging.debug(i)
    logging.debug('end')

if __name__ == '__main__':
    i = 10
    t1 = multiprocessing.Process(target=worker1, args=(i,))
    t1.daemon = True # デーモンプロセスにする
    t2 = multiprocessing.Process(name='renamed worker2', target=worker2, args=(i,))
    t1.start()
    t2.start()
    t2.join()
    t1.join()