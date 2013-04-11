#!coding=utf-8

import os ,traceback
import time


'''
fork()系统调用是Unix下以自身进程创建子进程的系统调用，一次调用，两次返回，如果返回是0，
则是子进程，如果返回值>0，则是父进程（返回值是子进程的pid）
'''
source = 10

i = 0
try:
    print '***********************'
    pid = os.fork()   #这里会返回两次，所以下面的省略号会输出2次
    print '......'
    if pid == 0:#子进程
        print "this is child process"

        source = source - 1

        print 'child process source is ',source
        time.sleep(18)

        print 'child sleep done'

    else:   #父进程
        print "this is parent process"

        print 'parent process source is ',source

        time.sleep(10)
        print 'parent sleep done'

    print source
except:
    traceback.print_exc()
