#! -*- coding=utf-8 -*-

#多线程的服务器,使用线程池

'''
线程池通常包含以下几个部分：
1.一个主要的侦听线程来接受和分派客户端的连接
2.一些工作者线程来处理客户端的请求
3.一个线程管理系统来处理那些意外终止的线程
'''

import socket,traceback
import os, sys,time
from threading import *

host=''
port=51423

#最大线程数
MAXTHREADS = 3

lockpool= Lock()  #引入互斥锁，访问同一个资源，只有获得锁的人，才能访问

#繁忙的线程
busylist = {}

#正在等待的线程
waitinglist = {}

#暂时存放不能处理的客户端连接
queue = []

'''
Semaphore（信号量）是计算机科学史上最古老的同步指令之一。Semaphore管理一个内置的计数器，每当调用acquire()时-1
，调用release() 时+1。计数器不能小于0；当计数器为0时，acquire()将阻塞线程至同步锁定状态，直到其他线程调用release()。

基于这个特点，Semaphore经常用来同步一些有“访客上限”的对象，比如连接池。
'''
sem = Semaphore(0)


def handleconnection(clientsock):
    """handle an incoming connection"""
    '''
   当一个线程调用Lock对象的acquire()方法获得锁时，这把锁就进入“locked”状态。因为每次只有一个线程1可以获得锁，
   所以如果此时另一个线程2试图获得这个锁，该线程2就会变为“blo同步阻塞状态。
   直到拥有锁的线程1调用锁的release()方法释放锁之后，该锁进入“unlocked”状态。
   线程调度程序从处于同步阻塞状态的线程中选择一个来获得锁，并使得该线程进入运行（running）状态。
    '''

    #获得锁
    lockpool.acquire()

    print "received new client connetcion"
    try:
        #检查当前是否达到了线程的 最大数
        if len(waitinglist) == 0 and (activeCount()-1)>=MAXTHREADS:
            clientsock.close()
            return

        #如果正在等待中的线程数为0，则开启新的线程
        if len(waitinglist) == 0:
            startthread()


        queue.append(clientsock)
        sem.release()
    finally:
        lockpool.release()


def startthread():
    # called by handleconnection when a new thread is needed
    # note: lockpool is already acquired where this function is called

    print "starting new client processor thread"

    t = Thread( target= threadwork)

    t.setDaemon(1)   #只要主线程完成了，不管子线程是否完成，都要和主线程一起退出

    t.start()


def threadwork():
    global waitinglist,lockpool,busylist

    time.sleep(1) #simulate expensive startup

    name = currentThread().getName()

    try:
        lockpool.acquire()
        try:
            waitinglist[name] = 1

        finally:
            lockpool.release()
        processclient()
    finally:
        if name in waitinglist:
            del waitinglist[name]

        if name in busylist:
            del busylist[name]

    startthread()


def processclient():
    """main loop of client-processing threads"""
    global sem,queue,waitinglist,lockpool,busylist

    name = currentThread().getName()

    while 1:
        sem.acquire()
        lockpool.acquire()

        try:
            clientsock = queue.pop(0)
            del waitinglist[name]
            busylist[name] = 1
        finally:
            lockpool.release()

        try:
            print "[%s] Got connection from %s"%\
            (name, clientsock.getpeername())

            clientsock.sendall("gettings .you are being serviced by %s.\n"%name)

            while 1:
                data = clientsock.recv(4096)
                if data.starstwith('DIE'):
                    sys.exit(0)
                if not len(data):
                    break
                clientsock.sendall(data)
        except(KeyboardInterrupt,SystemExit):
            raise
        except:
            traceback.print_exc()

        #close the connection

        try:
            clientsock.close()
        except KeyboardInterrupt:
            raise
        except:
            traceback.print_exc()
        lockpool.acquire()

        try:
            del busylist[name]
            waitinglist[name]=1
        finally:
            lockpool.release()


def listener():
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)

    s.bind((host, port))

    s.listen(1)

    while 1:
        try:
            clientsock,clientaddr = s.accept()
        except KeyboardInterrupt:
            raise   #自己触发异常
        except:
            traceback.print_exc()
            continue
        handleconnection(clientsock)



listener()







