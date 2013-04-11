#! -*- coding=utf-8 -*-

#-------------------------------------------------------------------------------
# Name:        tcp 客户端
# Purpose:   请求quux.org 的首页，这里的/表示首页,这里的70端口，是本来就是这样的，网站本来就是开放的
 # 70 端口
#
#运行方式  : python client.py quux.org /
#
# Author:      jack
#
# Created:     26/02/2013
# Copyright:   (c) jack 2013
# Licence:     <your licence>
#-------------------------------------------------------------------------------



import socket,sys

port=70

host = sys.argv[1]

filename=sys.argv[2]


s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)


#寻找端口号
#port = socket.getserverbyname('http','tcp')  #（协议名，端口号） 端口号是一个字符窜，例如http 可以被转换为一个端口号

try:
    s.connect((host,port))  #连接到服务器
except socket.gaierror,e:
    print "Error connecting to server:%s"%(e)
    sys.exit(1)


#显示本机的地址和端口号
s.getsockname()

#显示远端服务器的访问IP地址和端口号
s.getpeername()



'''
#第一种方式 直接发送信息到服务端
s.sendall(filename+"\r\n")
while 1:
    buf = s.recv(2048)
    if not len(buf):
        break
    sys.stdout.write(buf)
'''

#第二种方式

fd = s.makefile('rw',0) #操作文件类的模式和缓存的模式，操作文件类的模式可以是只读，只写或者读写，
                        #缓存主要用在磁盘文件，但是对于交互式的网络程序，它可能会阻碍程序的运行，所以
						#最好是设置为0，关闭它

fd.write(filename+"\r\n")

for line in fd.readlines():
    sys.stdout.write(line)

fd.close()

