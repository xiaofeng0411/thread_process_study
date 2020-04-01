'''
@Author: huxiaofeng
@Date  : 2020-03-29 20:27
'''

import threading
import time


def run(n):
    print("task", n)
    time.sleep(2)


start_time = time.time()
for i in range(50):
    t = threading.Thread(target=run, args=("t-%s"%i,))
    t.start()

print("cost:", time.time()-start_time)
