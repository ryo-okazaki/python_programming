import logging
import queue
import threading
import time

logging.basicConfig(level=logging.DEBUG, format='%(threadName)s: %(message)s')

def worker1(queue):
    logging.debug('start')

    while True:
        item = queue.get()
        if item is None:
            break
        logging.debug(item)
        queue.task_done()

    queue.put(100) # [100]
    time.sleep(5)
    queue.put(200) # [100, 200]

    logging.debug('end')

if __name__ == '__main__':
    queue = queue.Queue()
    for i in range(10):
        queue.put(i)
    t1 = threading.Thread(target=worker1, args=(queue,))
    t1.start()

    logging.debug('tasks are not done')
    queue.join() # queueが空になるまで待つ
    # for文でqueueに10個値をいれているので、queue.task_done()が10回呼ばれるまで待つ
    logging.debug('tasks are done')
    queue.put(None)

    t1.join()