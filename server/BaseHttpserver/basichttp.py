#! -*- coding=utf-8 -*-
'''
简单的http服务器、
只能同时处理一个请求
'''


from BaseHTTPServer import HTTPServer,BaseHTTPRequestHandler

class RequestHandler(BaseHTTPRequestHandler):
    def _writeheaders(self):
        self.send_response(200)
        self.send_header('Content-type','text/html')
        self.end_headers()

    def do_HEAD(self):   #处理http 请求的head方法
        self._writeheaders()

    def do_GET(self):     #处理http 请求的get方法
        self._writeheaders()
        self.wfile.write(" 'test'")

    def do_POST(self):    #处理http 请求的post方法
        self._writeheaders()
        self.wfile.write(" 'test'")



serveradd = ('',8765)

print 'server start'
srvr = HTTPServer(serveradd,RequestHandler)
srvr.serve_forever()
print 'server end'
