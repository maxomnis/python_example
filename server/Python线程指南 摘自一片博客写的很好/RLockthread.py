# encoding: UTF-8
import threading
import time


#RLock（可重入锁）是一个可以被同一个线程请求多次的同步指令
#。RLock使用了“拥有的线程”和“递归等级”的概念，处于锁定状态时
#，RLock被某个线程拥有。拥有RLock的线程可以再次调用acquire()，释放锁时需要调用release()相同次数。
rlock = threading.RLock()

def func():
    # 第一次请求锁定
    print '%s acquire lock...\n' % threading.currentThread().getName()
    if rlock.acquire():
        print '%s get the lock...\n' % threading.currentThread().getName()
        time.sleep(2)

        # 第二次请求锁定
        print '%s acquire lock again...\n' % threading.currentThread().getName()
        if rlock.acquire():
            print '%s get the lock...\n' % threading.currentThread().getName()
            time.sleep(2)

        # 第一次释放锁
        print '%s release lock...\n' % threading.currentThread().getName()
        rlock.release()
        time.sleep(2)

        # 第二次释放锁
        print '%s release lock...\n' % threading.currentThread().getName()
        rlock.release()

t1 = threading.Thread(target=func)
t2 = threading.Thread(target=func)
t3 = threading.Thread(target=func)
t1.start()
t2.start()
t3.start()