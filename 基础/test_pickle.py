#-------------------------------------------------------------------------------
# Name:        使用pickle模块，pickle模块将对象序列化为一个字节流，然后再还原,picket数据保存的格式，可能有出息版本的问题，格式是python特有的，其他语言不兼容
#              shevel 模块也有类似的功能，他是将数据保存为一个字典，但是有限制，键值必须是字符串，其次shevel中存储的值必须与pickle兼容
# Purpose:
#
# Author:      jack
#
# Created:     19/07/2012
# Copyright:   (c) jack 2012
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import pickle

class Test(object):
    def test():
        print "hello"

obj = Test()
f = open('test.txt','wb')  #是二进制
pickle.dump(obj,f)   # 将对象保存为二进制
f.close()


f = open('text.text','rb')
obj = pickle.load(f)
f.close()        #将二进制还原为对象