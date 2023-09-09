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
    with multiprocessing.Pool(5) as p:
        # r = p.map(worker1, [100, 200, 300]) # 並列化して処理を実行する
        # # 全てプロセスの処理が終わって、結果が返ってきてから、次の行を実行する
        # logging.debug('executed')
        # logging.debug(r)

        r = p.map_async(worker1, [100, 200, 300])
        logging.debug('executed')
        logging.debug(r.get())

        r = p.imap(worker1, [100, 200, 300])
        logging.debug('executed')
        # logging.debug(r.get([i for i in r]))
        for i in r:
            logging.debug(i)