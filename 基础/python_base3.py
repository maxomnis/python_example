#! coding=utf-8


#当控制流离开with语句后面的代码块时，with语句将自动关闭已打开的文件
with open('test.txt','w') as f:
    f.write('....')
    f.write('hhhhhh')


'''
with obj 语句在控制流进入和离开其后的相关代码时，允许obj管理所发生的事情。
执行with obj 语句时，它执行方法obj.__enter__()。当控制流离开时，就会执行
obj.__exit__(type,value,traceback),如果没有引发一场，__exit__()方法的3个
参数均被设置为None，否则，他们将包含于导致控制流离开上下文的异常相关的类型
，值和跟踪信息。__exit__()方法返回True或者False, 分别指示被引发的异常是否
得到了处理，如果返回False, 引发的任何异常都将被传递出上下文。

with obj 语句接受一个可选的as var说明符，如果指定了该说明符，obj.__enter__()
方法的返回值保存var中，


with 语句只支持上下文管理协议（__enter__()和__exit__())方法）的对象有效，
用户定义的类可以实现这些方法，从而定义自己的自定义上下文管理。
'''

class ListTransaction(object):
    def __init__(self, thelist):
        self.thelist = thelist

    def __enter__(self):
        self.working = list(self.thelist)
        print 'enter....'
        return self.working

    def __exit__(self, type, valua ,ta):    # 这个类对现在列表进行了一系列的修改，只有没有发生异常时，这些修改才会生效
        if type == None:
            pass
        print 'end....'
        return False

items = [1, 2, 3]

with ListTransaction(items) as working:
    working.append(4)
    working.append(5)

print working
print items




#contextlib 模块提供了一个装饰器和一些实用工具函数，用于创建与with语句结合使用的上下文管理器

from contextlib import contextmanager

@contextmanager
def ListTransaction(thelist):
    working = list(thelist)
    yield working
    thelist[:] = working

items = [6, 72, 8]

with ListTransaction(items) as working:
    working.append(4)
    working.append(5)

print items








