#! -*- coding=utf-8 -*-

#-------------------------------------------------------------------------------
# Name:        避免死锁 tcp客户端
# Purpose:
#
# Author:      jack
#
# Created:     01/03/2013
# Copyright:   (c) jack 2013
# Licence:     <your licence>
#-------------------------------------------------------------------------------


import socket,sys

port=51423

host='localhost'

data = "x"*10485760  #10 MB of data    10485760= 1024 * 1024 * 10

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

s.connect((host,port))

byteswritten=0

while byteswritten<len(data):
    starpos = byteswritten

	#每次发送1024个字节
    endpos = min(byteswritten+1024,len(data))

	#发送数据到服务器 ，可是10M的数据是永远发送不完的,服务器会读取开始的4KB(这个值不确定，不同的机子可能不同)，
	#不停的重复这个过程。因为客户端在发送完所有数据之前没有进行任何的读取，（  服务器（echoserver.py)，会将客户端
	#发送的数据返回给客户端，但是客户端这边没有接受数据)) ，操作系统的传输buffer 在某个一点上就会被充满，两个进程
	#就会在send()函数停滞。

	#解决办法:
	# 1.确保客户端每次执行完send()之后，进行一次recv()
	# 2.使客户端发送较少的数据（如10485760改为1024）
	# 3. 使用多线程和其他一些方法，是客户端同时接收和发送
    byteswritten += s.send(data[starpos:endpos])
    s.recv(1024)


    sys.stdout.write("Wrote %d bytes\r"%byteswritten)
    sys.stdout.flush()


#清除缓存内容
s.shutdown(1)

while 1:
    buf = s.recv(1024)
    if not len(buf):
        break
    sys.stdout.write(buf)
