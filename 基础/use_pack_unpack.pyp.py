# coding=utf-8

#-------------------------------------------------------------------------------
# Name:        将数据转换为二进制字节流，用于网络传输
# Purpose:
#
# Author:      jack
#
# Created:     13/04/2013
# Copyright:   (c) jack 2013
# Licence:     <your licence>
#-------------------------------------------------------------------------------


import struct


"""
struct.pack用于将Python的值根据格式符，转换为字符串（因为Python中没有字节(Byte)类型，可以把这里的字符串理解为字节流，或字节数组）
"""
a = 20

b = 400


str = struct.pack('ii',a,b)

print 'length:', len(str)

print str

print repr(str)


print '--------------------------'


"""
struct.unpack 用于将字节流转换成python数据类型
"""
str = struct.pack('ii',a ,b )

a1,b1 = struct.unpack('ii',str)

print 'a1:' ,a1

print 'b1:', b1


"""
struct.calcsize用于计算格式字符串所对应的结果的长度，如：struct.calcsize('ii')，返回8。因为两个int类型所占用的长度是8个字节。
"""
print struct.calcsize('si')



a = 12.34

byte = struct.pack('f',a)   #注意这里是字符串类型用f，而非i

a = struct.unpack('f', byte)   #unpack返回的是tump

#print a     输出 (12,)

print a



a = 'hello'
b='world!'
c=2
e=2000
d=45.12

byte = struct.pack('5s6s2if',a ,b ,c ,e ,d)

print byte





f = '你hao'

s = struct.pack('s',f)

name = struct.unpack('s',s)
print name

