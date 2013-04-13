#!/usr/bin/env python
# coding=gbk

#-------------------------------------------------------------------------------
# Name:        StringIo, cString 将内存写在内存里面，而非磁盘
# Purpose:
#
# Author:      jack
#
# Created:     13/04/2013
# Copyright:   (c) jack 2013
# Licence:     <your licence>
#-------------------------------------------------------------------------------


import StringIO, cStringIO, sys

s = StringIO.StringIO('')

s.write("中国")
s.write("湖北")
s.write("仙桃")

print s.getvalue()

s.seek(0)
print s.read()

#从最后8个字节开始读取
s.seek(-8,2)
print s.read()

s.seek(10)
print s.tell()


