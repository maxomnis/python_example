#! coding=utf-8

#-------------------------------------------------------------------------------
# Name:        对象表示和属性绑定
# Purpose:
#
# Author:      jack
#
# Created:     31/03/2013
# Copyright:   (c) jack 2013
# Licence:     <your licence>
#-------------------------------------------------------------------------------


#只要使用了obj.name= value ,就会调用特殊的方法obj.__setattr__("name",value)
#del obj.name  就会调用特殊的方法obj._delattr__("name")
#查找属性 obj.name 就会调用obj.__getattribute__("name")

'''
__slots__ 使用

定义__slots__ 后，可以再实例上分配的属性名称将被限制为指定的名称。否则将引发AttributeError,
这种限制可以阻止其他人向现有的实例添加新的属性.

使用__slots__的类的实例不在使用字典来存储数据。相反，会使用基于数组的更加紧凑的数据结构。
在会创建大量对象的程序中，使用__slots__可以显著减少内存占用和使用时间
'''
class Account(object):
    __jakc='11'
    __ren__ = 'account'
    __slots__ = ('name' ,'balance')



class Account2(Account):
    __test__ = 'hello'
    __slots__ = ( 'age')

class Test(object):
    def __init__(self ,name):
        self.name = name









#抽象基类  ,抽象基类并不能直接实例化,但是基类的方法可以直接在之类中调用 Foo.spam(a,b)

from abc import ABCMeta, abstractmethod,abstractproperty

class Foo:    #python3.0 中使用 class Foo(metaclass=ABCMeta)

    __metaclass__  = ABCMeta

    @abstractmethod
    def spam(self, a, b):
        pass

    @abstractproperty
    def name(self):
        pass


#抽象基类支持对已经存在的类进行注册，使其属于该基类,使用register()方法

class Grok(object):
    def test(self, a ,b):
        print 'grok'

#向Foo抽象基类注册
Foo.register(Grok)

'''
向抽象基类注册某个类时，对于注册类中的实例，涉及抽象基类的类型检查操作(isinstance(),issubclass()),将返回True
，向抽象类注册某个类时，不会检查该类是否实际实现了任何抽象方法或者特性，这种注册过程只会影响类型检查。它不会
像一家注册的类进行额外的错误检查。
'''













