#! -*- coding=utf-8 -*-
#-------------------------------------------------------------------------------
# Name:  生产者通知消费者不再生产任何项目
# Purpose:
#
# Author:      jack
#
# Created:     13/01/2013
# Copyright:   (c) jack 2013
# Licence:     <your licence>
#-------------------------------------------------------------------------------


import multiprocessing

def consumer(input_q):
    while True:
        item = input_q.get()
        if item is None:
            break

        #处理项目
        print(item)
    #关闭
    print("consumer done")

def producer(sequence,output_q):
    for item in sequence:
        output_q.put(item)



if __name__ == '__main__':
    q = multiprocessing.Queue()

    cons_p = multiprocessing.Process(target=consumer,args=(q,))
    cons_p.start()

    #生产项目
    sequence = [1,2,3,4,5,6]
    producer(sequence,q)

    #在队列上安置标志，发出完成信号
    q.put(None)

    #等待使用者进程关闭
    cons_p.join()
