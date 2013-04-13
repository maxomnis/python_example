#! coding=utf-8
#-------------------------------------------------------------------------------
# Name:        python 模拟post提交数据
# Purpose:
#
# Author:      jack
#
# Created:     02/04/2013
# Copyright:   (c) jack 2013
# Licence:     <your licence>
#-------------------------------------------------------------------------------


import urllib
import urllib2
import json
'''
url = 'http://192.168.1.42/cgi-bin/award.cgi'

values = {
    'act' :'jump',
    'data' : '{day:5, money:100}'
}

data = json.dumps(values)
print data

temp = json.loads(data)
print temp
req = urllib2.Request(url, data)

response = urllib2.urlopen(req)

page = response.read()
print page
'''


url ='http://192.168.1.42/cgi-bin/award.cgi?act=jump&data=100'
f = urllib.urlopen(url)
print f.read()