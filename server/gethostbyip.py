#! -*- coding=utf-8 -*-

#-------------------------------------------------------------------------------
# Name:        根据IP查域名
# Purpose:
#
# Author:      jack
#
# Created:     08/03/2013
# Copyright:   (c) jack 2013
# Licence:     <your licence>
#-------------------------------------------------------------------------------


import socket
import sys

#

try:
    result = socket.gethostbyaddr(sys.argv[1])
    print "primary hostname:"
    print " "+result[0]

    print "\n address:"
    for item in result[2]:
        print " "+item

except socket.herror,e:
    print "couldn't look up name:",e