#! -*- coding=utf-8 -*-
#-------------------------------------------------------------------------------
# Name:        multiprocessing
# Purpose:
# 进程的使用
#
# Author:      jack
#
# Created:     09/01/2013
# Copyright:   (c) jack 2013
# Licence:     <your licence>
#-------------------------------------------------------------------------------


import multiprocessing
import time

def clock(interval):
    while True:
        print("the time is %s"%time.ctime)
        time.sleep(interval)

def main():
    p = multiprocessing.Process(target=clock,args=(1,))
    p.start()   #启动进程，并调用子进程中的p.run方法

if __name__ == '__main__':
    main()
