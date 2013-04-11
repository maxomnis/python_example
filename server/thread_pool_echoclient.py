#! -*- coding=utf-8 -*-

import socket,sys

port=51423

host='localhost'

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

s.connect((host,port))


while 1:
    data = sys.stdin.readline().strip()
    #data = trim(data)

    #如果发送数据为空，则客户端会卡死，如果加上数据为空的处理，跳出循环，则正常
    #if not len(data):
    #    print "data is none"
    #    continue

    s.send(data)
    buf = s.recv(1024)
    if not len(buf):
        break
    sys.stdout.write(buf)
