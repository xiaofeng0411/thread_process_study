'''
@Author: huxiaofeng
@Date  : 2020-04-01 21:33
'''

import threading
import time


def run(n):
    print('task',n)
    time.sleep(2)
    print("task done",n)


start_time = time.time()
t_objs = []
for i in range(50):
    t = threading.Thread(target=run,args='t-%s'%i,)
    t.start()
    t_objs.append(t)


for t in t_objs:
    t.join()


print("------all threads has finished" ,threading.current_thread())
print("cost:",time.time() -start_time)
