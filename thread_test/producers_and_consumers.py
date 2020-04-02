'''
@Author: huxiaofeng
@Date  : 2020-04-02 22:45
'''

import queue
import threading
import time

q=queue.Queue(maxsize=10)


def Producer(name):
    count = 1
    while True:
        q.put("骨头%s" % count)
        print('生产了%s骨头'%count)
        count += 1


def Consumer(name):
    while True:
        print('[%s]取到【%s】,eat' % (name, q.get()))
        time.sleep(1)



p = threading.Thread(target=Producer, args=('Alex',))
c = threading.Thread(target=Consumer, args=('niu',))
c1 = threading.Thread(target=Consumer, args=('hu',))


p.start()
c.start()
c1.start()
