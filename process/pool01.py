#! -*- coding=utf-8 -*-

#-------------------------------------------------------------------------------
# Name:        进程池
# Purpose:
#
# Author:      jack
#
# Created:     15/01/2013
# Copyright:   (c) jack 2013
# Licence:     <your licence>
#-------------------------------------------------------------------------------



import os

import multiprocessing

import hashlib

BUSIZE = 8192 #读取缓存区大小

POOLSIZE=2 #工作进程的数量

def compute_digst(filename):
    try :
        f = open(filename,'rb')
    except IOError:
        return None
    digest = hashlib._sha512
    while True:
        chunk  = f.read(BUSIZE)
        if not chunk:
            break
        digest.update(chunk)
    f.close()
    return filename,digest.digest()

def build_digest_map(topdir):
    digest_pool = multiprocessing.Pool(POOLSIZE)
    allfiles = (os.path.join(path,name)
                   for path,dirs,files in os.walk(topdir)
                       for name in files)
    digest_map = dict(digest_pool.imap_unordered(compute_digst,allfiles,20))
    digest_pool.close()
    return digest_map

if __name__ == '__main__':
    digest_map = build_digest_map("d:\\")
    print(len(digest_map))
