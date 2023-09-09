import logging
import queue
import threading
import time

logging.basicConfig(level=logging.DEBUG, format='%(threadName)s: %(message)s')

def worker1(barrier):
    r = barrier.wait() # ロックを取得
    logging.debug('num={}'.format(r))
    while True:
        logging.debug('start')
        time.sleep(3)
        logging.debug('end')

def worker2(barrier):
    r = barrier.wait() # ロックを取得
    logging.debug('num={}'.format(r))
    while True:
        logging.debug('start')
        time.sleep(3)
        logging.debug('end')

if __name__ == '__main__':
    barrier = threading.Barrier(2) # 必ず2つのスレッドが立ち上がってから実行される
    t1 = threading.Thread(target=worker1, args=(barrier,))
    t2 = threading.Thread(target=worker2, args=(barrier,))
    t1.start()
    t2.start()

    # クライアントとサーバー側で両方スレッドが立ち上がっていないと実行できない仕様の時に使う