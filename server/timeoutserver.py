#! -*- coding=utf-8 -*-

#-------------------------------------------------------------------------------
# Name:        超时设置
# Purpose:
#
# Author:      jack
#
# Created:     01/03/2013
# Copyright:   (c) jack 2013
# Licence:     <your licence>
#-------------------------------------------------------------------------------



import socket,traceback
import sys

host=''
port=51423

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

s.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)

s.bind((host,port))

s.listen(1)

while 1:
    try:
        clientsock,slientadd = s.accept()
    except KeyboardInterrupt:
        raise
    except:
        traceback.print_exc()
        continue
    else:
        "accept successful!"


    clientsock.settimeout(5)  #超过五秒钟如果没有任何东西发过来，连接就中断

    try:
        print "Got connection from",clientsock.getpeername()
        while 1:
            data = clientsock.recv(4096)
            if not len(data):
                break
            clientsock.sendall(data)
    except( KeyboardInterrupt,SystemExit):
        raise
    except socket.timeout:
        traceback.print_exc()
        #sys.exit('time out ........')

    except:
        traceback.print_exc()

    try:
        clientsock.close()
    except KeyboardInterrupt:
        raise
    except:
        traceback.print_exc()

