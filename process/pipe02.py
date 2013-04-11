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

#服务器处理
def adder(pipe):
    server_p,client_p = pipe
    client_p.close()
    while True:
        try:
            x,y = server_p.recv()
        except EOFError:
            break
        result=x+y
        server_p.send(result)

    #关闭
    print("Server done")




if __name__ == '__main__':
    (server_p,client_p) = multiprocessing.Pipe()

    #启动服务器进程
    adder_p = multiprocessing.Process(target=adder,args=((server_p,client_p),))
    adder_p.start()

    #关闭客户端中的服务器管道
    server_p.close()


    #在服务器上提出一些请求
    client_p.send((3,4),)

    #客户端接受返回的数据
    print(client_p.recv())

    client_p.send(('hello','world'),)
    print(client_p.recv())

    #完成,关闭管道
    client_p.close()

    #等待消费者进程关闭
    adder_p.join()

    print '......'