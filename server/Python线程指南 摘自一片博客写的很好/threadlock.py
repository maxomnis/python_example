# encoding: UTF-8
import threading
import time

data = 0
lock = threading.Lock()

def func():
    global data
    print '%s acquire lock...\n' % threading.currentThread().getName()

    # 调用acquire([timeout])时，线程将一直阻塞，
    # 直到获得锁定或者直到timeout秒后（timeout参数可选）。
    # 返回是否获得锁。
    if lock.acquire():
        print '%s get the lock.\n' % threading.currentThread().getName()
        data += 1
        time.sleep(1)
        print '%s release lock...\n' % threading.currentThread().getName()

        # 调用release()将释放锁。
        lock.release()

t1 = threading.Thread(target=func)
t2 = threading.Thread(target=func)
t3 = threading.Thread(target=func)
t1.start()
t2.start()
t3.start()