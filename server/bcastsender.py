#! -*- coding=utf-8 -*-

#-------------------------------------------------------------------------------
# Name:        广播发送端
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
import sys

host=''
port = 51423

dest = ('<broadcast>',51423)

s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

s.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)

try:
    s.sendto("hello",dest)
except:
    traceback.print_exc()
    sys.exit;

print "Lookling for replies"

while 1:
    try:
        (buf,address) = s.recvfrom(2048)
        if not len(buf):
            break
        print "received from %s:%s" %(address,buf)

    except(KeyboardInterrupt,SystemExit):
        raise
    except:
        traceback.print_exc()
