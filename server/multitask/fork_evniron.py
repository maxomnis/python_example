#! coding=utf-8

#copy-on-write技术
'''
意思上就是：在复制一个对象的时候并不是真正的把原先的对象复制到内存的另外一个位置上，
而是在新对象的内存映射表中设置一个指针，指向源对象的位置，并把那块内存的Copy-On-Write位设置为1.
这样，在对新的对象执行读操作的时候，内存数据不发生任何变动，直接执行读操作；而在对新的对象执行写操作时，
将真正的对象复制到新的内存地址中，并修改新对象的内存映射表指向这个新的位置，并在新的内存位置上执行写操作。
'''

import os
from os import environ

def my_fork():
    environ['foo'] = "aaaaaaaa"
    print "foo environmental variable set to:%s" % (environ['foo'])

    environ['foo'] = "bbbbbbbb"
    print "foo environmental variable changed to:%s" % (environ['foo'])

    child_pid = os.fork()

    if child_pid == 0:
        print "child process :pid # %s"%os.getpid()
        print "child foo environmental variable == %s " %(environ['foo'])
    else:
        print "parent process :pid # %s"%os.getpid()
        print "parent foo environmental variable == %s " %(environ['foo'])

if __name__ == "__main__":
    my_fork()

'''
[sislcb@gm_247 python]$ python fork_evniron.py
foo environmental variable set to:aaaaaaaa
foo environmental variable changed to:bbbbbbbb
child process :pid # 12577
child foo environmental variable == bbbbbbbb
parent process :pid # 12576
parent foo environmental variable == bbbbbbbb

'''