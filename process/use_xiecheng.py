#! coding=utf-8

#-------------------------------------------------------------------------------
# Name:        协成
# Purpose:
#
# Author:      jack
#
# Created:     30/03/2013
# Copyright:   (c) jack 2013
# Licence:     <your licence>
#-------------------------------------------------------------------------------

'''
把函数编写为一个任务，从而能处理发送给他的一系列输入，这种函数称为协程
'''

def print_matchs(matchtext):
    print "looking for",matchtext
    while True:
        line = (yield)     #用 yield语句并以表达式（yield)的形式创建协程
        if matchtext in line:
            print line


'''
>>> matcher = print_matchs('python')
>>> matcher.next()
looking for python
>>> matcher.send('hello python')
hello python
>>> matcher.send('test')
>>> matcher.send('python is cool')
python is cool
>>>matcher.close()
'''

