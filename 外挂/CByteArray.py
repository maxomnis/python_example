#!usr/lib/python
# -*- coding:gb2312 -*-
"""

"""
from struct import pack,unpack
import binascii
import md5
from types import StringType

try:
    from cStringIO import StringIO
except ImportError:
    from StringIO import StringIO


class CByteArray():
    """ """
    ENDIAN_LETTLE           =   1
    ENDIAN_BIG              =   0

    def __init__(self,buf=None):
        """ """
        self.__buf = StringIO()
        if isinstance(buf,StringType):
            self.__buf.write(buf)
        self.endian = CByteArray.ENDIAN_BIG;
        self.position = 0;
    def readShort(self):
        """ """
        fmt =   "%sh"%self._isEndian()
        res = unpack(fmt,self._readbuf(2))
        return res[0]

    def readInt(self):
        """ """
        fmt =   "%si"%self._isEndian()
        res =   unpack(fmt,self._readbuf(4))
        return res[0]

    def readFloat(self):
        """ """
        fmt =   "%sf"%self._isEndian()
        res =   unpack(fmt,self._readbuf(4))
        return res[0]

    def readDouble(self):
        """ """
        fmt =   "%sd"%self._isEndian()
        res =   unpack(fmt,self._readbuf(8))
        return res[0]

    def readUTFBytes(self,nlen):
        """ """
        fmt =   "%ss"%(nlen)
        res =   unpack(fmt,self._readbuf(nlen))
        return res[0]

    def readByte(self):
        """ """
        fmt =   "%sb"%self._isEndian()
        res =   unpack(fmt,self._readbuf(1))
        return res[0]

    def writeShort(self,value):
        """ """
        assert(type(value) == int)
        fmt =   "%sh"%self._isEndian()
        self._addbuf(pack(fmt,value))

    def writeInt(self,value):
        """ """
        assert(type(value) == int)
        fmt =   "%si"%self._isEndian()
        self._addbuf(pack(fmt,value))

    def writeFloat(self,value):
        assert(type(value) == float)
        fmt =   "%sf"%self._isEndian()
        self._addbuf(pack(fmt,value))

    def writeDouble(self,value):
        """ """
        fmt =   "%sd"%self._isEndian()
        self._addbuf(pack(fmt,value))

    def writeUTFBytes(self,value):#转换数据为字节类型
        """ """
        assert(type(value) == StringType)
        fmt =   "%ss"%(len(value))
        self._addbuf(pack(fmt,value))

    def writeByte(self,value):
        fmt = "%sb"%self._isEndian()
        self._addbuf(pack(fmt,value))

    def getvalue(self):
        """ """
        return self.__buf.getvalue();

    def length(self):
        """ """
        old_pos =   self.__buf.tell();
        self.__buf.seek(0,2);
        nlen =  self.__buf.tell();
        self.__buf.seek(old_pos);
        return nlen

    def _addbuf(self,value):
        """ """
        old_pos =   self.__buf.tell();  #当前
        if old_pos != self.position:
            self.__buf.seek(self.position)
        self.__buf.write(value)
        self.position = self.__buf.tell()

    def _readbuf(self,nlen):
        """ """
        old_pos =   self.__buf.tell();
        if old_pos != self.position:
            self.__buf.seek(self.position);
        buf =    self.__buf.read(nlen);
        self.position   +=  nlen
        return buf;

    def _isEndian(self):
        """ """
        if self.endian == CByteArray.ENDIAN_BIG:
            return ">"
        else:
            return ""

class ByteArray(CByteArray):
    """ """
    def __init__(self,buf=None):
        """ """
        CByteArray.__init__(self,buf)

def get_md5(tmp):
    n = md5.new(tmp)
    return n.hexdigest().lower()


if __name__ == "__main__":
   # print get_md5('123456')
    data = CByteArray('')
    data.writeShort(0)
    data.writeShort(1)
    data.writeShort(len("jack"))
    data.writeUTFBytes("jack")

    data.writeShort(len("e10adc3949ba59abbe56e057f20f883e"))
    data.writeUTFBytes("e10adc3949ba59abbe56e057f20f883e")
    data.endian = CByteArray.ENDIAN_LETTLE
    data.position =0
    data.writeShort(data.length())
    print binascii.hexlify(data.getvalue())

