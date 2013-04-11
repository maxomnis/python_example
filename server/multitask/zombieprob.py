#! coding=utf-8


#在子进程终止和父进程调用wait()之间的这段时间，子进程被称为zombie进程，它停掉了运行
#但是内存结构还为运行父进程执行wait()保持着

#ZOMBIE：僵尸状态。表示进程结束但尚未消亡的一种状态。此时进程已经结束运行并释放大部分资源，但尚未释放进程控制块。

#os.fork()是唯一一个返回两次的函数，在调用fork()之后，就同时存在两个您正在运行的程序的拷贝。

'''
在一个fork()之后 ，每个进程都有一个不同的地址空间，更改一个进程中的变量，不会影响其他的
进程中的变量，这是和thread的一个主要不同，这就使您的代码减少了被攻击的可能

一个进程的fork拷贝是一个准确的拷贝，它继承了父进程的所有文件描述符和 socket,所以可能遇到一种情况就是，
父进程和 子进程对一个单一的远程主机，都有一个开放的连接。

这并不好，1。两个进程都试图通过socket通信，结果可能混淆，另外一点是，两个进程都要调用了close()，连接才能真正的被
关闭。

init的角色

init程序总是系统运行的第一个进程，他的pid是1，它主要角色是启动和关闭系统
init还有另外一个角色，如果一个进程死掉了，系统中还有该进程的子进程（可能是
zombie)，系统将改变子进程的父进程Pid为1（也就是init的进程id)，init程序会像
普通进程那样观察有zombie问题的子进程，这些子进程将被清理

'''

import os,time

print "before the fork ,my pid is",os.getpid()

pid = os.fork()

if pid:
    print "hello from the parent, the child will be pid %d",pid
    print "sleeping 120s"
    time.sleep(120)


