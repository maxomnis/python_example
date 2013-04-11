#! -*- coding=utf-8 -*-
#-------------------------------------------------------------------------------
# multiprocessing 支持进程间的通信方式有两种：管道和队列
#
# Name:        Queue   创建共享的进程队列
#              JoinableQueue   创建可连接的共享进程队列,但是JoinableQueue队列允许项目的使用者通知生产者项目已经被处理完
# Purpose:
#
# Author:      jack
#
# Created:     09/01/2013
# Copyright:   (c) jack 2013
# Licence:     <your licence>
#-------------------------------------------------------------------------------



import multiprocessing

def consumer(input_q):
    while True:
        item = input_q.get()

        #处理项目
        print (item)      #此处替换为有用的工作

        #发出信号通知任务完成
        input_q.task_done()


def producer(sequence,out_q):
    for item in sequence:

        #将项目放入队列
        out_q.put(item)

if __name__ == '__main__':

    #创建共享进程队列
    q = multiprocessing.JoinableQueue()

    #创建使用者进程，调用consumer方法，给consumer传递参数q
    cons_p = multiprocessing.Process(target=consumer,args=(q,))

    cons_p.daemon = True   #指示是否是后台进程，当创建它的python进程终止时，后台进程将自动终止，并且禁止后台进程创建自己的进程

    cons_p.start() #启动进程，这将允许代表进程的子进程，并调用子进程中的run()方法



    sequence = [4,5,6,1,2,444,1,2,3,4]
    producer(sequence,q)

    #join() 使用者使用此方法进行阻塞，直到队列中的所有项目均被处理,
    q.join()

    print cons_p.is_alive()
    print cons_p.name
    print cons_p.pid
