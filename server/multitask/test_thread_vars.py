#!coding=utf-8
#使用线程共享变量

import threading
#全局变量
a=50
b=50

c=50

d=50

def printvars():
    print "a=",a
    print "b=",b
    print "c=",c
    print "d=",d


def threadcode():
    #如果你想要为一个定义在函数外的变量赋值，那么你就得告诉Python这个变量名不是局部的，
    #而是 全局 的。我们使用global语句完成这一功能。没有global语句，是不可能为定义在函数外的变量赋值的。
    global a,b,c,d
    a+=50;
    b=+50
    c=100
    d="hello"
    print "[childthread values of variable in child thread:"
    printvars()

print "[mainthread] values of variables before child chread:"
printvars()

t = threading.Thread(target=threadcode, name="ChildThread")

t.setDaemon(1)

t.start()

t.join()



print "[mainthread] values of variables after child thread:"
printvars()

