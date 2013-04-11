#! -*- coding=utf-8 -*-

#-------------------------------------------------------------------------------
# Name:        模块1
# Purpose:
#
# Author:      jack
#
# Created:     08/03/2013
# Copyright:   (c) jack 2013
# Licence:     <your licence>
#-------------------------------------------------------------------------------


import struct
import sys

def htons(num):
    return struct.pack('!H',num)  #

def htonl(num):
    return  struct.pack('!I',num)

def ntohs(data):
    return struct.unpack('!H',data)[0]

def ntohl(data):
    return struct.unpack('!I',data)[0]

def sendstring(data):
    return htonl(len(data))+'    '+data

print "Enter a string:"

str = sys.stdin.readline().strip()

print repr(sendstring(str))

