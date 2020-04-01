'''
@Author: huxiaofeng
@Date  : 2020-04-01 23:25
'''

#互斥锁同时只允许一个线程更改数据，而semapjore是同时允许一定数量的线程更改数据，比如厕所有3个。那最多有
#三个人同时上厕所


import threading,time


def run(n):
    semaphore.acquire()
    time.sleep(1)
    print('run the thread:%s\n'%n)
    semaphore.release()


if __name__ == '__main__':
    num = 0
    semaphore = threading.BoundedSemaphore(5)
    for i in range(20):
        t = threading.Thread(target=run,args=(i,))
        t.start()


while threading.active_count() != 1:
    pass

else:
    print('______all threads done----')
    print(num)

