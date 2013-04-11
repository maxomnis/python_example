#! -*- coding=utf-8 -*-

#-------------------------------------------------------------------------------
# Name:        管道
# Purpose:
#
# Author:      jack
#
# Created:     14/01/2013
# Copyright:   (c) jack 2013
# Licence:     <your licence>
#-------------------------------------------------------------------------------



import multiprocessing

def consumer(pipe):
    output_p,input_p = pipe

    #关闭输入管道
    input_p.close()

    while True:
        try:
            item = output_p.recv() #接受
        except EOFError:
            break

        #处理项目
        print (item)

    print("consumer done")


#生产项目并将其放置到队列上,sequence代表要处理项目的可迭代对象

def producer(sequence,input_p):
    for item in sequence:
        #将项目放在队列上
        input_p.send(item)

if __name__ == '__main__':

    #创建管道
    #(output_p,input_p) = multiprocessing.Pipe()
    pips = (output_p,input_p) = multiprocessing.Pipe()

    #启动线程
    cons_p = multiprocessing.Process(target=consumer,args=(pips,))
    cons_p.start()


    #关闭生产者中的输出管道
    output_p.close()                      #如果生产者或者消费者中都没有使用管道的某个端点，就应该将其关闭，这也说明了为何在生产者中关闭了管道的输出端
                                           #在消费者中关闭管道的输入端，如果忘记执行这些操作，程序可能在recv()操作上挂起

    #生产项目
    sequence = [1,2,3,4,5]
    producer(sequence,input_p)

    #关闭输入管道，表示完成
    input_p.close()

    #等待使用者进程关闭
    cons_p.join()
