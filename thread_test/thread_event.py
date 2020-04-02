'''
@Author: huxiaofeng
@Date  : 2020-04-02 21:48
'''
import threading
import time


event = threading.Event()


def lighter():
    count = 0
    event.set()
    while True:
        if count > 20 and count <= 30:
            event.clear()
            print("red light")
        elif count >30:
            event.set()
            count = 0
        else:
            print("green light")
        time.sleep(1)
        count += 1


def car(name):
    while True:
        if event.is_set():
            print("[%s]running"%name)
            time.sleep(1)
        else:
            print('[%s]waiting'%name)
            event.wait()
            print('start going')


light = threading.Thread(target=lighter,)
light.start()

car = threading.Thread(target=car,args=('tesila',))
car.start()