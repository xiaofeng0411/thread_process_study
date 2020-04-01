'''
@Author: huxiaofeng
@Date  : 2020-04-01 22:43
'''

import threading
import time


def run(n):
    # add lock
    lock.acquire()
    global num
    num += 1
    # release lock
    lock.release()

num = 0
lock = threading.lock()

t_objs = []
for i in range(10000):
    t = threading.Thread(target=run,args=('t-%s'%i,))
    t.start()
    t_objs.append(t)


for t in t_objs:
    t.join()


print("------all threads has finished" ,threading.current_thread())
print(num)
