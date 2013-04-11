#! coding=utf-8

#-------------------------------------------------------------------------------
# Name:        yield 生成器使用
# Purpose:    使用yield，可以让函数生成一个结果序列
#
# Author:      jack
#
# Created:     30/03/2013
# Copyright:   (c) jack 2013
# Licence:     <your licence>
#-------------------------------------------------------------------------------


def countdown(n):
    print "counting down!"
    while n >0:
        print 'aaaaa'
        yield n
        n -=1
        print 'bbbbb'