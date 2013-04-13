#! -*- coding:utf-8 -*-
#-------------------------------------------------------------------------------
# Name:        tcp 服务端
# Purpose:
#  首先运行这个代码，然后telnet 127.0.0.1  51423  这个测试该端口是否打开，输入字符串
#  并且一次只能处理一个请求，只有前天的请求断开后，后面的请求才会有响应.
#
#  http://192.168.1.6:51423 也是可以访问的，因为http请求本来就是基于TCP的socket连接
#
# Author:      jack
#
# Created:     26/02/2013
# Copyright:   (c) jack 2013
# Licence:     <your licence>
#-------------------------------------------------------------------------------



import socket


host=''                #监听所有的来访
#host='192.168.1.6'    #绑定到本服务器的IP，外网也可以访问
#host='127.0.0.1'      #只有服务器本地才可以访问
#host='192.168.1.42'   # 非本服务器IP，绑定会报错
port = 51423

port = 80        #绑定到小于1024的端口，需要root用户

#建立socket对象 ,

# socket.socket（协议,通讯方式） 创建socket对象
# socket.AF_INET使用PIV4协议；
# socket.SOCK_STREAM TCP通讯方式
# socket.SOCK_DGTAM UDP通讯方式


s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

#设置socket选项
s.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)  #socket.SO_REUSEADDR服务器程序关闭之后，立马释放端口

# setcoketpet(level,optname,value)   level 定义哪个选项被使用，通常情况下是SOL_SOCKET，它的意思是正在使用的socket选项，

#绑定socket

'''
s.bind(('',80)) ,绑定到80端口,它是标准的http(web)端口，然而操作系统通常约定限制小于1024的端口号，这样一来
只有root用户可以绑定他们，
'''
s.bind((host,port))


#侦听连接
'''
这个调用通知操作系统准备收连接，它只是一个参数，这个参指明了再服务器实际处理连接的时候，允许有多少个等待的连接在队列中等待，
作为一个约定，很多人设置为5（很多操作系统根本不支持大于5），对于多任务，多线程的服务器来说，这个意义不大，但是是必须的
'''
s.listen(1)

print "Server is running on port %d;press Ctrl-c to terminate."\
%port



while 1:

    '''
    通常情况下，无限循环是不好的，因为他会耗尽系统的CPU资源，这里的循环是不同的，当你调用accept的时候，它只在一个客户端连接后才
     返回，同时，你的程序停止，并不使用任何CPU资源，一个停止并等待或者输入的程序被称作阻塞程序
     '''
    clientsock,clientadd = s.accept()   #程序在这里阻塞，等待连接
    clientfile = clientsock.makefile('rw',0)
    clientfile.write("Welcome, "+str(clientadd)+"\n")
    clientfile.write("Please enter a string :")

    line = clientfile.readline().strip()#在这里等待输入
    clientfile.write("You entered %s characters.\n"%line)
    clientfile.close()    #最后注释掉之后，第一个链接，然后第二个链接时，第一个链接会断掉，
    clientsock.close()
