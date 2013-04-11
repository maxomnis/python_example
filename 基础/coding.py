#coding=utf-8
a= u'中国'

b = a.encode('utf8')

c = b.decode('utf8')
import sys
print sys.stdin.encoding
print sys.stdout.encoding
print b
print c