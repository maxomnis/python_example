#-------------------------------------------------------------------------------
# Name:        ʹ��pickleģ�飬pickleģ�齫�������л�Ϊһ���ֽ�����Ȼ���ٻ�ԭ,picket���ݱ���ĸ�ʽ�������г�Ϣ�汾�����⣬��ʽ��python���еģ��������Բ�����
#              shevel ģ��Ҳ�����ƵĹ��ܣ����ǽ����ݱ���Ϊһ���ֵ䣬���������ƣ���ֵ�������ַ��������shevel�д洢��ֵ������pickle����
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
f = open('test.txt','wb')  #�Ƕ�����
pickle.dump(obj,f)   # �����󱣴�Ϊ������
f.close()


f = open('text.text','rb')
obj = pickle.load(f)
f.close()        #�������ƻ�ԭΪ����