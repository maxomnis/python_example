#! coding=utf-8
#-------------------------------------------------------------------------------
# Name:        创建子进程，每隔15秒打印一次，
# Purpose:
#
# Author:      jack
#
# Created:     28/03/2013
# Copyright:   (c) jack 2013
# Licence:     <your licence>
#-------------------------------------------------------------------------------


import multiprocessing
import time

class ClockProcess(multiprocessing.Process):
    def __init__(self , intval):
        multiprocessing.Process.__init__(self)
        self.intval = intval

    def run(self):
        while 1:
            print "time is %s" % time.time()
            time.sleep(self.intval)


if __name__ == '__main__':
    p = ClockProcess(5) #创建了一个子进程
    p.start()
