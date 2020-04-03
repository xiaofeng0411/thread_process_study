'''
@Author: huxiaofeng
@Date  : 2020-04-03 21:49
'''

from multiprocessing import Process,Queue


#进程中资源不共享


def f(q):
    q.put([42,None,'hello'])


if __name__ == '__main__':
    q = Queue()
    p = Process(target=f,args=(q,))
    p.start()
    print(q.get())
    p.join()