#! coding=utf-8
#-------------------------------------------------------------------------------
# Name:        python基础操作
# Purpose:
#
# Author:      jack
#
# Created:     29/03/2013
# Copyright:   (c) jack 2013
# Licence:     <your licence>
#-------------------------------------------------------------------------------


#高级字符串格式化  {n}占位符将被format()方法的位置参数n所替代
r = "{0} {1} {2}".format('good', 100,12)

#关键字占位符
r = "{name} {shares} {price}".format(name="good" , shares=100, price = 10.11)


#字典操作
#键的值可以是任意不可变的对象，如字符串，数字和数组

d = {}

d[(0,1,2,3)] = "foo"

#print d[(0,1,2,3)]


#集合操
t = set([1,2,3])
f = set([2,4,5])

print t|f   #求t ,f 的并集

print t & f   #求t,f的交集

print t-f  #求 t,f的差集

print t ^ f #求t,f的对称差集


# chr将整数转换为字符
print chr(100)

#将字符转换为其整数值
print ord('a')



a = 1
b = 1

print (a is b)





try:
    print '....'
except IOError as e:     #except Exception ,e:  这种语法在2.6中，已经废弃了
    #处理I/O错误
    print '....'
except NameError as e:
    print '....'

except (IOError, TypeError, NameError) as e:
    print '...'

except Exception as e:   #使用EXception 可以捕捉除了与程序退出有关的所有之外的所有异常
    print '...'

except :               #捕捉所有的异常
    print '....'

else:                #如果没有引发异常，就会执行
    print '.....'

finally:           #无论发生什么都会执行
    print '.....'





