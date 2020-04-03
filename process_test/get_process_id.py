'''
@Author: huxiaofeng
@Date  : 2020-04-03 21:30
'''
from multiprocessing import Process
import os

#每一个进程都是由父进程启动


def info(title):
    print(title)
    print('module name',__name__)
    print('parent process',os.getppid())
    print('process id',os.getpid())
    print('\n\n')


def f(name):
    info('\033[31;i an function f\033[0m')
    print('hello',name)


if __name__ == "__main__":
    info('\033[31;i an main process line\033[0m')
    p = Process(target=f,args=('bob',))
    p.start()
    p.join()