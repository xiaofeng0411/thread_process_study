'''
@Author: huxiaofeng
@Date  : 2020-04-02 22:31
'''


import queue

#first in first out
q=queue.Queue()
#last in first out
q=queue.LifoQueue()
#primary
q = queue.PriorityQueue()
q.put((1,1))
q.put((2,-1))
q.put((3,3))
q.put((4,10))


print(q.get())