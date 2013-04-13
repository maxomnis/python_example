#! -*- coding=utf-8 -*-

import socket,sys
from struct import pack,unpack
from CByteArray import CByteArray
port=443

host = sys.argv[1]

def ooo():
    data = CByteArray()

    # data = 长度 + 消息 + 其他内容
    data.writeShort(0)

    data.writeShort(1)

    data.writeShort(len("jack"))
    data.writeUTFBytes("jack")

    data.writeShort(len("e10adc3949ba59abbe56e057f20f883e"))
    data.writeUTFBytes("e10adc3949ba59abbe56e057f20f883e")

    data.endian = CByteArray.ENDIAN_LETTLE
    data.position =0
    data.writeShort(data.length())
    print data.length()
    return (data.getvalue())

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)


try:
    s.connect((host,port))  #连接到服务器
except socket.gaierror,e:
    print "Error connecting to server:%s"%(e)
    sys.exit(1)


#第一种方式 直接发送信息到服务端
s.sendall(ooo())
while 1:
    buf = s.recv(2048)
    if not len(buf):
        break
    sys.stdout.write(buf)
    data = CByteArray(buf)

    data.readShort()
    data.readShort()
    uid = data.readInt()


    print uid


