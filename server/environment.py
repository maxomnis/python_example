#! -*- coding=utf-8 -*-

#-------------------------------------------------------------------------------
# Name:        获得环境信息
# Purpose:
#
# Author:      jack
#
# Created:     08/03/2013
# Copyright:   (c) jack 2013
# Licence:     <your licence>
#-------------------------------------------------------------------------------


import socket
import sys

def getipaddrs(hostname):
    result = socket.getaddrinfo(hostname,None,0,socket.SOCK_STREAM)
    return [x[4][0] for x in result]


hostname = socket.gethostname()  #获取本机名

print "host name:",hostname

print "fully-qualified name:",socket.getfqdn(hostname)#获得完整的数据

try:
    print "IP addresses:",", ".join(getipaddrs(hostname))
except socket.gaierror ,e:
    print "couldn't not get ip address:",e


