#! -*- coding=utf-8 -*-

#-------------------------------------------------------------------------------
# Name:        模块1
# Purpose:
#  查看机器上安装的python 所支持的socket选项
# Author:      jack
#
# Created:     27/02/2013
# Copyright:   (c) jack 2013
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import socket

solist = [x for x in dir(socket) if x.startswith('SO_')]
solist.sort()

for x in solist:
    print x