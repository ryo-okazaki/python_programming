import logging
import multiprocessing
import time

logging.basicConfig(level=logging.DEBUG, format='%(processName)s: %(message)s')

def worker1(i):
    logging.debug('start')
    time.sleep(5)
    logging.debug('end')
    return i

if __name__ == '__main__':
    # t1 = multiprocessing.Process(target=worker1, args=(i,))
    with multiprocessing.Pool(5) as p:
        p1 = p.apply_async(worker1, (100,))
        p2 = p.apply_async(worker1, (100,))
        logging.debug('executed')
        logging.debug(p1.get(timeout=1))
        logging.debug(p2.get())
    # プールを使うと、複数のプロセスを使って処理を実行できる
    # 非同期で並列化