# encoding: UTF-8
import threading
import time

# 计数器初值为2
semaphore = threading.Semaphore(2)

def func():

    # 请求Semaphore，成功后计数器-1；计数器为0时阻塞
    print '%s acquire semaphore...\n' % threading.currentThread().getName()
    if semaphore.acquire():

        print '%s get semaphore...\n' % threading.currentThread().getName()
        time.sleep(4)

        # 释放Semaphore，计数器+1
        print '%s release semaphore...\n' % threading.currentThread().getName()
        semaphore.release()

t1 = threading.Thread(target=func)
t2 = threading.Thread(target=func)
t3 = threading.Thread(target=func)
t4 = threading.Thread(target=func)
t1.start()
t2.start()
t3.start()
t4.start()

time.sleep(2)

# 没有获得semaphore的主线程也可以调用release
# 若使用BoundedSemaphore，t4释放semaphore时将抛出异常
print 'MainThread release semaphore without acquire'
semaphore.release()