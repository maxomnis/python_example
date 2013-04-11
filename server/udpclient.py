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





while 1:
    print "Enter data to transmit:"
    #读取数据发送给服务端
    data = sys.stdin.readline().strip()
    s.sendall(data)
	
	#接收服务器返回的数据
    buf = s.recv(2048)
	
	#如果返回数据为空则退出客户端
    if not len(buf):
        break
    sys.stdout.write('你输入的数据是:'+buf+"\n")

