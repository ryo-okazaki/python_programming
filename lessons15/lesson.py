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

def worker2(x, y=1):
    logging.debug('start')
    logging.debug(x)
    logging.debug(y)
    # print(threading.currentThread().getName(), 'start')
    time.sleep(2)
    logging.debug('end')
    # print(threading.currentThread().getName(), 'end')

# if __name__ == '__main__':
#     t1 = threading.Thread(name='rename worker1', target=worker1)
#     t2 = threading.Thread(target=worker2, args=(100, ), kwargs={'y': 200})
#     t1.start()
#     t2.start()
#     print('started')

if __name__ == '__main__':
    # threads = []
    # for _ in range(5):
    #     t = threading.Thread(target=worker1)
    #     t.setDaemon(True)
    #     t.start()
    #     threads.append(t)
    # # for thread in threads:
    # #     print('before join', thread.is_alive())
    # #     thread.join()
    # #     print('after join', thread.is_alive())
    # for thread in threading.enumerate():
    #     if thread is threading.currentThread():
    #         print('current thread')
    #         continue
    #     thread.join()

    t = threading.Timer(3, worker1)
    t2 = threading.Timer(3, worker2, args=(100,), kwargs={'y': 200})
    t.start()
    t2.start()

    # t2 = threading.Thread(target=worker2)
    # t2.setDaemon(True)
    # t1.start()
    # t2.start()
    # print('started')
    # t1.join() # t1が終わるまで待つ 強制終了しない デーモン化した場合に記述する