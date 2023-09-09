import queue
from multiprocessing.managers import BaseManager

queue = queue.Queue()

class QueueManager(BaseManager):
    pass

QueueManager.register('get_queue', callable=lambda: queue)

manager = QueueManager(
    address=('0.0.0.0', 50000),
    authkey=b'abracadabra'
)
server = manager.get_server()
server.serve_forever()