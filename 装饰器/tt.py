import time

def foo():
    print 'in foo()'

def timeit(func):
    start = time.clock()
    func()
    end =time.clock()
    print 'used:', end - start

timeit(foo)