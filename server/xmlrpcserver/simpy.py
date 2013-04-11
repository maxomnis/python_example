#! -*- coding=utf-8 -*-

#simplexmlrpcserver 第一个例子  远程调用，把本地的函数，给远程的调用

from SimpleXMLRPCServer import SimpleXMLRPCServer,SimpleXMLRPCRequestHandler
from SocketServer import ThreadingMixIn
import traceback


class Math:
    def pow(self,x,y):
        return x*y
    def hex(self,x):
        return "%x" % x

class ThreadingServer(ThreadingMixIn, SimpleXMLRPCServer):
    pass

serveraddr = ('',8765)

srvr = ThreadingServer(serveraddr, SimpleXMLRPCRequestHandler)

srvr.register_instance(Math())

srvr.register_introspection_functions()

srvr.serve_forever()

