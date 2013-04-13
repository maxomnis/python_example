#!/usr/bin/python
# -*- coding:gb2312 -*-
#=======================================================
#@author:jeffxun
#@date  : 2012/12/12
#@context: 
#=======================================================

from pyamf.amf3 import ByteArray

class PackBase:
    def __init__(self,msg):
        """ """
        self.msg    =   msg;
        self.__createByteArray(msg);
        
    def __createByteArray(self,msg):
        """ """
        self.buf = ByteArray();
        self.buf.writeShort(0);
        self.buf.writeShort(msg);
        
    def strLen(self,nstr):
        """"""
        if isinstance(nstr,int):
            nstr = str(nstr)
        bnstr =  ByteArray()
        bnstr.writeUTFBytes(nstr);
        return len(bnstr);
        
    def pack(self):
        """ """
        self.buf.seek(0);
        self.buf.endian = ByteArray.ENDIAN_LITTLE;
        self.buf.writeShort(len(self.buf));
        return self.buf.getvalue();
        
class unPackBase(object):
    def __init__(self,buf):
        """ """
        self.buf = ByteArray(buf);
        
        