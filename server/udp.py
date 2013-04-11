#! -*- encoding=utf-8 -*-
#-------------------------------------------------------------------------------
# Name:        udp 客户端
# Purpose:
#
# Author:      jack
#
# Created:     26/02/2013
# Copyright:   (c) jack 2013
# Licence:     <your licence>
#-------------------------------------------------------------------------------



import socket,sys

host = sys.argv[1]

textport = sys.argv[2]


s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

try:
    port = int(textport)
except ValueError:
    port = socket.getserverbyname(textport,'udp')

s.connect((host,port))

print "Enter data to transmit:"
data = sys.stdin.readline().strip()

s.sendall(data)


while 1:
    buf = s.recv(2048)
    if not len(buf):
        break
    sys.stdout.write(buf)

