#! -*- coding=utf-8 -*-

#-------------------------------------------------------------------------------
# Name:  根据域名查IP
# Purpose:
#
# Author:      jack
#
# Created:     08/03/2013
# Copyright:   (c) jack 2013
# Licence:     <your licence>
#-------------------------------------------------------------------------------


import sys
import socket

#根据域名查IP
result = socket.getaddrinfo(sys.argv[1],None,0,socket.SOCK_STREAM)
#print result

#result 返回的是一个元组

counter=0
for item in result:            #result 可能会返回多个结果，根据不同的协议返回的不同，如果有些协议没有被配置，则可能只有一个结果
                               #限制结果，让每个条目只显示一次，可以为protocol设定值
    print "%-2d:%s" % (counter,item[4])
    counter+=1


