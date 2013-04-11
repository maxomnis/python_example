#！ -*- coding=utf-8 -*-

'''
SimpleHTTPServer 类扩展了BaseHTTPServer类

这个程序会输出当前目录（以及它子目录）里面的文件
'''

from BaseHTTPServer import HTTPServer
from SimpleHTTPServer import SimpleHTTPRequestHandler

serveradd = ('',8765)
srvr = HTTPServer(serveradd,SimpleHTTPRequestHandler)
srvr.serve_forever()