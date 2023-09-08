import logging
import threading
import time

logging.basicConfig(level=logging.DEBUG, format='%(threadName)s: %(message)s')

def worker1():
    logging.debug('start')
    # print(threading.currentThread().getName(), 'start')
    time.sleep(5)
    logging.debug('end')
    # print(threading.currentThread().getName(), 'end')

def worker2():
    logging.debug('start')
    # print(threading.currentThread().getName(), 'start')
    time.sleep(5)
    logging.debug('end')
    # print(threading.currentThread().getName(), 'end')

if __name__ == '__main__':
    t1 = threading.Thread(target=worker1)
    t2 = threading.Thread(target=worker2)
    t1.start()
    t2.start()
    print('started')