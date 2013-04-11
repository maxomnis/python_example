# encoding: UTF-8
import threading
import time

'''
Event（事件）是最简单的线程通信机制之一：一个线程通知事件，其他线程等待事件。
Event内置了一个初始为False的标志，当调用set()时设为True，调用clear()时重置为 False
。wait()将阻塞线程至等待阻塞状态。
'''

event = threading.Event()

def func():
    # 等待事件，进入等待阻塞状态
    print '%s wait for event...' % threading.currentThread().getName()
    event.wait()

    # 收到事件后进入运行状态
    print '%s recv event.' % threading.currentThread().getName()

t1 = threading.Thread(target=func)
t2 = threading.Thread(target=func)
t1.start()
t2.start()

time.sleep(2)

# 发送事件通知
print 'MainThread set event.'
event.set()