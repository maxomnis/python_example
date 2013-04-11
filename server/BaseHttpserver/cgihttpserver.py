#! -*- coding=utf-8 -*-

'''
cgihttpserver 和simplehttpserver类似,cgi文件一般放在服务器根目录的cgi-bin目录下，
使用cgihttpserver ，在当前目录也可以执行，不过还是得改权限为可执行
'''

from BaseHTTPServer import HTTPServer

from CGIHTTPServer import CGIHTTPRequestHandler

from SocketServer import ThreadingMixIn

class ThreadingServer(ThreadingMixIn,HTTPServer):
    pass

serveradd = ('',8765)

print 'server start'
srvr = ThreadingServer(serveradd,CGIHTTPRequestHandler)
srvr.serve_forever()
print 'server end'

#http://localhost:8765/test.cgi 来访问