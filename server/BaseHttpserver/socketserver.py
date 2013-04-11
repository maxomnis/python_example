#! -*- coding=utf-8 -*-

'''
实现新协议
'''

from SocketServer import ThreadingMixIn,TCPServer,StreamRequestHandler
import time
import traceback

class TimeRequestHanlder(StreamRequestHandler):
    def handle(self):
        req = self.rfile.readline().strip()
        if req == "asctime":
            result = time.asctime()

        elif req == "second":
            result = str(int(time.time()))

        elif req == "rfc822":
            result = time.strftime("%a ,%d %b %Y %H:%M:%S +0000",time.gmtime())

        else:
            result = "helo -- \
            asctime ,second,rfc822"
        self.wfile.write(result+"\n")


class TimeServer(ThreadingMixIn,TCPServer):
    allow_reuse_address = 1000


serveradd=('',8765)

try:
    srvr = TimeServer(serveradd,TimeRequestHanlder)

    srvr.serve_forever()
except:
    traceback.print_exc()

