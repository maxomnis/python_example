#! -*- coding=utf-8 -*-
#-------------------------------------------------------------------------------
# Name:        实现进程，通过继承类PROCESS
# Purpose:
#
# Author:      jack
#
# Created:     09/01/2013
# Copyright:   (c) jack 2013
# Licence:     <your licence>
#-------------------------------------------------------------------------------




import multiprocessing
import time

class Clock(multiprocessing.Process):
    def __init__(self,interval):
        multiprocessing.Process.__init__(self)
        self.interval = interval

    def run(self):
        while True:
            print("the time is %s"% time.ctime())
            time.sleep(self.interval)


if __name__ == '__main__':
    p = Clock(2)
    p.start()
