import logging
import queue
import threading
import time

logging.basicConfig(level=logging.DEBUG, format='%(threadName)s: %(message)s')

def worker1(queue):
    logging.debug('start')

    queue.put(100) # [100]
    time.sleep(5)
    queue.put(200) # [100, 200]

    logging.debug('end')

def worker2(queue):
    logging.debug('start')

    logging.debug(queue.get())
    logging.debug(queue.get()) # 値が入ってくるまで待ち続ける
    # スレッド間でデータを入れたり出したりする時に使う

    logging.debug('end')

if __name__ == '__main__':
    queue = queue.Queue()
    t1 = threading.Thread(target=worker1, args=(queue,))
    t2 = threading.Thread(target=worker2, args=(queue,))
    t1.start()
    t2.start()
    print('started')