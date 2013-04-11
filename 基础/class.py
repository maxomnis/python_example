#!coding=utf-8

#python 类的定义
class Account(object):
    num_accounts = 0    #此处的 num_accounts 为类变量，所有的实例共享
    def __init__(self,name,blance):  #__init__ 在类的实例创建后被立即调用。它可能会引诱你称之为类的构造函数，
	                                 #但这种说法并不正确。说它引诱，是因为它看上去像 (按照习惯，__init__ 是类中第一个定义的方法)，
									 #行为也像 (在一个新创建的类实例中，它是首先被执行的代码)，并且叫起来也像 
									 #(“init”当然意味着构造的本性)。说它不正确，是因为对象在调用 __init__ 时已经被构造出来了，
									 #你已经有了一个对类的新实例的有效引用。但 __init__ 是在 Python 中你可以得到的最接近构造函数的东西，
									 #并且它也扮演着非常相似的角色。
        self.name = name
        self.blance = blance
        Account.num_accounts +=1

    def __del__(self):
        Account.num_accounts-=1

    def inqirey(self):
        return self.blance

#__init__ 方法是可选的，但是一旦你定义了，就必须记得显示调用父类的 __init__ 方法 
#(如果它定义了的话)。这样更是正确的：无论何时子类想扩展父类的行为，后代方法必须在适当的时机，使用适当的参数，显式调用父类方法

#访问类的成员的方法
print Account.num_accounts
print Account.__init__

class Money(object):
    def __init__(self,types,num,name,action):
        self.types = types
        self.num = num
        self.name=name

class Test(Money,Account):#python类的多继承，python虽然支持多继承，但是最好使用单继承，免得混淆
    def inqirey(self):
        super(Test,self).inqirey() #调用父类的inqirey()方法
    print "hello"
    pass

#t = test('jack',4)

#print Test.__mro__   要找到使用了多重继承的属性，可以在列表中队所有基类按从“最特殊”的类到“最不特殊的类这种进行排列，
#然后再搜索属性时，就会按账号顺序搜索列表，直到找到该属性
#第一个定义,对于任何一个类，通过打印它的__mro__属性即可看到基类的顺序，例如Test类中的name属性，如果要打印name属性，到底是Money,中的name，还是Account的name,是按照基类的继承属性来的

#@staticmethod 静态方法是一种普通函数，就位于类定义的命名空间中，它不会对任何实例类进程操作，
#如果在编写类时需要采用很多种不同方式来创建新实例，则常常使用静态方法
import time
class Date(object):
    def __init__(self,year,month,day):
        self.year = year
        self.month = month
        self.day = day

    def test(self):
        print "hello"
    @staticmethod
    def now():
        t = time.localtime()
        return Date(t.tm_year,t.tm_mon,t.tm_mday)
    @staticmethod
    def tomorrrow():
        t  = time.localtime(time.time()+86400)
        return Date(t.tm_year,t.tm_mon,t.tm_mday)

a = Date(1967,4,5)
b = Date.now()
print b.day

c = Date.tomorrrow()
print c.day


#@clssmethod 类方法是将类本身作为对象进行操作的方法,与实例方法不同，因为根据约定，类是作为第一个参数（名为cls)传递的,实例方法是self作为第一个参数
class Times(object):
    factor = 1
    @classmethod
    def mul(cls,x):
        return cls.factor*x

class TwoTimes(Times):
    factor = 2

x = TwoTimes.mul(4)  #调用Times.mul(TwoTimes,4)


#@property  支持以简单形式访问后面的方法，无需像平常一样添加额外的()调用该方法
import math
c = None
class Circle(object):
    def __init__(self,radius):
        self.radius = radius
    @property
    def area(self):
        return math.pi*self.radius**2

c = Circle(5)
print c.area


#数据封装和私有属性
#私有属性，其他子类是不能访问的
#类中所有以双下划线(__)例如：__foo ,都会自动变形，形成具有_类名__foox形式的新名称，这提供了一种在类中包含私有属性和私有方法的有效方式
#，因为派生类中使用的私有名称不会与
#基类中使用的相同私有名称发生冲突

class A(object):
    def __init__(self):
        self.__x = 3        #变形为self._A__x
    def __spam(self):
        pass                #变形为_A__spam()
    def bar(self):
        self.__spam         #调用A.__spam()

class B(A):
    def __init__(self):
        A.__init__(self)
        self.__x = 37
    def __spam(self):
        print "hello"                #变形为_B__spam()



class T(object):
    __slots__ = ('name','blance')
    def __init__(self):
        self.name = 'jack'
        self.blance = '120'
        self.hometowm='wuhan'


class M(T):
    pass





