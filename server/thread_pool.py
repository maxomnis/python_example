#!coding=utf-8

#用Python创建线程池

import time
import threading
import Queue
class Worker(threading.Thread):
    def __init__(self, name, queue):
        threading.Thread.__init__(self)
        self.queue = queue
        self.start()
    def run(self):
        # 著名的死循环，保证接着跑下一个任务
        while True:
            # 队列为空则退出线程
            if self.queue.empty():
                break
            # 获取一个项目
            foo = self.queue.get()
            # 延时1S模拟你要做的事情
            time.sleep(1)
            # 打印
            print '%s\t\t%s\n'%(self.getName(),foo)
            # 告诉系统说任务完成
            self.queue.task_done()
# 队列
queue = Queue.Queue()
# 加入100个任务队列
for i in range(100):
    queue.put(i)
# 开10个线程
for i in range(10):
    threadName = 'Thread' + str(i)
    Worker(threadName, queue)
# 所有线程执行完毕后关闭
queue.join()