#! -*- coding=utf-8 -*-

'''
scoket 长连接 服务端
'''
import socket
import sys
import time

def close_socket(sock) :
    try:
        sock.close()
    except socket.error, e :
        print 'Error close socket:%s' % e
    #else :
        #print 'Close socket successfully!'

def flush_socket(sock_fd) :
    try:
        sock_fd.flush()
    except socket.error, e:
        print 'Error flush the buffer:%s' % e
        return False
    else:
        #print 'Flush the buffer successfully'
        return True

def communicate(connection) :
    while True:

        #这里循环用于接收数据
        i=1
        while True:

            try:
                #print 'begin to rec'
                buf=connection.recv(2048)
                print "buf_"+str(i)+":"+buf

            except socket.error, e:
                print 'Error receiving data:%s' % e
                close_socket(connection)
                return
            if not len(buf):
                print 'Socket has been closed!'
                close_socket(connection)
                return
            if '\r\n' in buf : #\r\n is the terminator
                break

        print 'The receiving data is', buf

        if not flush_socket(sock_fd):
            close_socket(connection)
            return

        try:
            #print 'begin to send'
            connection.send('Welcome!\r\n')
            #print 'send ok'
        except socket.error, e:
            print 'Error sending data:%s' % e
            close_socket(connection)
            return

        if not flush_socket(sock_fd):
            close_socket(connection)
            return

if __name__ == '__main__':

    try:
        socket.setdefaulttimeout(2)  #2秒之后，如果没有链接过来，就超时
    except socket.error, e:
        print 'Strange error setdefaulttimeout:%s' % e
        sys.exit()

    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        #sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        #sock.setblocking(0)
    except socket.error, e:
        print 'Strange error creating socket:%s' % e
        sys.exit(1)

    print 'Create socket successfully'

    try:
        sock.bind(('localhost', 8650))
    except socket.error, e:
        print 'Strange error bind socket:%s' % e
        sys.exit(1)

    print 'Bind successfully'

    try:
        sock.listen(5)
    except socket.error, e:
        print 'Strange error begin to listen:%s' % e
        sys.exit(1)

    print 'Server - Begin to listened'

    while True:
        try:
            connection,address = sock.accept()
        except socket.error, e:
            print 'Strange error begin to accept:%s' % e
            continue

        try:
            sock_fd = connection.makefile('rw', 0)
        except socket.error, e:
            print 'Makefile error:%s' % e
            close_socket(connection)
            continue

        print 'Server - have accepted'

        communicate(connection)
