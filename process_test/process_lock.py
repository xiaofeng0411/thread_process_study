'''
@Author: huxiaofeng
@Date  : 2020-04-04 09:33
'''


from multiprocessing import Process,Lock


def f(l,i):
    l.acquire()
    try:
        print('hello world',i)
    finally:
        l.release()


if __name__ == '__main__':
    lock = Lock()
    for num in range(10):
        Process(target=f,args=(lock,num)).start()