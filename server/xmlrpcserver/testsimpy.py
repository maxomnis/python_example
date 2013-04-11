#! -*- coding=utf8 -*-

#测试xmlrpcserver

'''
运行该程序可以跟simpy.py 程序进行交谈，可以调用simpy 里面定义的pow(),和hex()函数，这个就是远程调用了


'''

import xmlrpclib, code

url = "http://localhost:8765/"

s = xmlrpclib.ServerProxy(url)

interp = code.InteractiveConsole({'s':s})

interp.interact("you can now use the object to interact where the server")