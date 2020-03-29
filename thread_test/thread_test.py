'''
@Author: huxiaofeng
@Date  : 2020-03-29 20:27
'''

import threading


def run(n):
    print("task",n)


t1 = threading.Thread(target=run,args=("t1",))
t2 = threading.Thread(target=run,args=("t2",))
t1.start()
t2.start()