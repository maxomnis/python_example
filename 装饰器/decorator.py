#! coding=utf-8

#装饰器

'''
经常被用于有切面需求的场景，较为经典的有插入日志、性能测试、事务处理等。装饰器是解决这类问题的绝佳设计，
有了装饰器，我们就可以抽离出大量函数中与函数功能本身无关的雷同代码并继续重用。概括的讲，装饰器的作用就是为已经存在的对象添加额外的功能。
'''



'''
import time

def foo():
    print 'in foo()'

# 定义一个计时器，传入一个，并返回另一个附加了计时功能的方法
def timeit(func):

    # 定义一个内嵌的包装函数，给传入的函数加上计时功能的包装
    def wrapper():
        start = time.clock()
        func()
        end =time.clock()
        print 'used:', end - start

    # 将包装后的函数返回
    return wrapper

foo = timeit(foo)
foo()
'''

import time

def timeit(func):
    def wrapper(a):
        start = time.clock()
        func(1,2)
        end =time.clock()
        print 'used:', end - start
        print a

    return wrapper

@timeit   #  foo = timeit(foo)完全等价, 使用之后,foo函数就变了，相当于是wrapper了
def foo(a,b):
    pass

#foo(1)


'''
foo = timeit(foo)
foo()
'''
'''
random_award(dbm , uid, stime, flag, oid):
fifteen_award(dbm, uid, awardtype, stime, flag, oid):
    user_award(dbm, uid, awardtype ,type,stime,flag,oid)
    random_award(dbm , uid, stime, flag, oid)

    check_post(db,stime,flag, uid, oid,id)



def check_post(fn):
    def worker(dbm,stime,flag,uid,old,id):
'''


def test(fn):
    def wraper(**kwgs):
        a = kwgs['a']

        pm = "tttttttttttttttt"
        for i in kwgs:
            print kwgs[i]
        fn(pm , **kwgs)
        print 'aaa'
    return wraper



@test
def home(t, **kwgs):
    print t
    print kwgs['a']

@test
def jack(**kwgs):
    print 'jack'
    print kwgs['a']

home(a=1,b=2,c=3)

#jack(a=1,b=2,c=3,k=10)


def worker(**kras):
    print kras



def worker(**kras):
    print kras
