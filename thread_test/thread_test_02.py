'''
@Author: huxiaofeng
@Date  : 2020-03-29 22:18
'''


import threading
import time


class MyThread(threading.Thread):
    def __init__(self,n):
        super(MyThread,self).__init__()
        self.n = n


    def run(self):
        print("runnint task",self.n)


t1 = MyThread("t1")
t2 = MyThread("t2")

t1.start()
t2.start()