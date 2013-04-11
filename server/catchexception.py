#! -*- coding=utf-8 -*-

#-------------------------------------------------------------------------------
# Name:        异常处理
# Purpose: 任何没有捕获的异常都会终止程序，所以服务端要处理任何可能发生的异常
#
#建议放置一个普通的错误处理来确保任何错误都不会从故障中漏掉
#

#建议使用try...finally 来关闭socket连接
# Author:      jack
#
# Created:     28/02/2013
# Copyright:   (c) jack 2013
# Licence:     <your licence>
#-------------------------------------------------------------------------------



import socket,traceback

host=''
port = 51423

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

s.setsocket(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)

s.bind((host,port))

s.listen(1)

while 1:
    try:
        clientsock,clientadd = s.accept()
    except (KeyboardInterrupt,SystemExit):
        raise

    except:
        traceback.print_exc()
        continue

    #Process the connection

    try:
        print "Got connection from",clientsock.getpeername()
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
