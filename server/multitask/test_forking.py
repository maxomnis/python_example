#! coding=utf-8

#forking 的第一步

import os
import time

print "before fork ,my pid is ", os.getpid()

#fork()会返回两次
if os.fork():
    print "hello from the parent. my pid is ",os.getpid() ,time.time()

else:
    print "hello from the child. my pid is ",os.getpid(),time.time()

time.sleep(10)
print "hello from both of us"


'''
before fork ,my pid is  12083
hello from the child. my pid is  12084 1363058998.17
hello from the parent. my pid is  12083 1363058998.17

hello from both of us 输出两次 ，程序的两个拷贝在运行
hello from both of us
'''