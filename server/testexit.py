#! -*- coding=utf-8
#-------------------------------------------------------------------------------
# Name:        模块1
# Purpose:
#
# Author:      jack
#
# Created:     28/02/2013
# Copyright:   (c) jack 2013
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import sys,traceback
def main():
    print'begin'                  #如果这里不捕捉异常的话，程序运行到打印出begin就结束了,final是不会被打印的
    try:
        sys.exit('exitok')
    except :
        print traceback.extract_stack()
    print'final'



if __name__ == '__main__':
    main()
