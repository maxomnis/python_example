#!coding=utf-8

import time,threading,sys

def sleepandprint(name):
    time.sleep(1)
    print name+" hello from both of us"

def threadcode():
    sys.stdout.write("hello from the new thread,my name is %s\n" % threading.currentThread().getName())
    sleepandprint("child thread")


print "before starting a new thread ,my name is", threading.currentThread().getName()

t = threading.Thread(target=threadcode,name="childThread")

t.setDaemon(1)

t.start()

sys.stdout.write("hello from the main thread. my name is %s\n" % threading.currentThread().getName())

sleepandprint("main thread")


#join方法，如果一个线程或者一个函数在执行过程中要调用另外一个线程，
#并且待到其完成以后才能接着执行，那么在调用这个线程时可以使用被调用线程的join方法。
t.join()