#! -*- coding=utf-8 -*-

#-------------------------------------------------------------------------------
# Name:        udp服务端
# Purpose:
#
# Author:      jack
#
# Created:     28/02/2013
# Copyright:   (c) jack 2013
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import socket,traceback

host=''
port = 20000

s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

s.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)

s.bind((host,port))

while 1:
    try:
        message,addrss = s.recvfrom(9182)#接受数据来自客户端，不需要用accept(),listen()
        print "Got date from",addrss
        s.sendto(message,addrss)
    except (KeyboardInterrupt,SystemExit):
        raise
    except:
        traceback.print_exc()


if __name__ == '__main__':
    main()
