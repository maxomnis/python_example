#! -*- coding=utf-8 -*-

'''
同时处理过个请求
SocketServer（以及其子类）提供了两种方法来解决多请求:
1.forking 是为每一个连接创建一个新的进程，所有这些进程都是独立的（在nuix平台上被广泛使用)

2.Threading 是使用Python thread 来处理连接，它并不区分不同的连接 (windows 必须使用这个，
绝大多数windows上的python不能实现forking)

3.noblocking (或者是异步asynchronous)通信,SocketServer不支持这种做法
'''


from BaseHTTPServer import HTTPServer,BaseHTTPRequestHandler
from SocketServer import ThreadingMixIn

import time ,threading

starttime = time.time()   #只要这个脚本开始运行，starttime变量就一直保存着，直到该服务器脚本停止为止

class RequestHandler(BaseHTTPRequestHandler):
    """ definition of request handler"""
    def _writeheader(self,doc):
        if doc is None:
            self.send_response(404)
        else:
            self.send_response(200)

        self.send_header('Content-type','text/html')
        self.end_headers()

    def _getdoc(self,filename):
        global starttime
        if filename =='/':
            return "test"
        elif filename == "/stats.html":
            return "server has been running for %d seconds"%(time.time() - starttime)
        else:
            return None

    def do_HEAD(self):
        doc = self._getdoc(self.path)
        self._writeheader(doc)

    def do_GET(self):
        doc = self._getdoc(self.path)
        print "Handling with thread",threading.currentThread().getName()#获取当前处理请求的线程的名字
        self._writeheader(doc)
        if doc is None:
            return "%s not found"%(doc)
        else:
            self.wfile.write(doc)

class ThreadingHTTPServer(ThreadingMixIn,HTTPServer):
    pass

serveradd = ('',8765)

print 'server start'
srvr = ThreadingHTTPServer(serveradd,RequestHandler)
srvr.serve_forever()

print 'server end'


#http://localhost:8765/stats.html 来访问



















