#!/usr/bin/env python
# coding=gbk

#-------------------------------------------------------------------------------
# Name:        StringIo, cString ���ڴ�д���ڴ����棬���Ǵ���
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

s.write("�й�")
s.write("����")
s.write("����")

print s.getvalue()

s.seek(0)
print s.read()

#�����8���ֽڿ�ʼ��ȡ
s.seek(-8,2)
print s.read()

s.seek(10)
print s.tell()


