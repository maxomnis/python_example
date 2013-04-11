#! -*- coding=utf-8 -*-

#-------------------------------------------------------------------------------
# Name:        使用广播  广播接收端
# Purpose:
#
# Author:      jack
#
# Created:     08/03/2013
# Copyright:   (c) jack 2013
# Licence:     <your licence>
#-------------------------------------------------------------------------------


import socket
import traceback

host=''
port = 51423

s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

s.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)

s.setsockopt(socket.SOL_SOCKET,socket.SO_BROADCAST,1)  #支持socket广播

s.bind((host,port))

while 1:
    try:
        message ,address = s.recvfrom(8192)
        print "god data from",address
        s.sendto("I am here",address)
    except(KeyboardInterrupt,SystemExit):
        raise
    except:
        traceback.print_exc()
