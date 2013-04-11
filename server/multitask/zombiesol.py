#! coding=utf-8

#使用信号解决zombie问题

import os, time, signal



def chldhandler(signum ,stackframe):

    while 1:
        try:
            result = os.waitpid(-1, os.WNOHANG)

        except:
            break
    signal.signal(signal.SIGCHLD, chldhandler)

#每次收到SIGCHLD信号，就调用chldhandler这个处理函数
signal.signal(signal.SIGCHLD, chldhandler)

'''
在一个进程终止或者停止时，将SIGCHLD信号发送给其父进程。按系统默认将忽略此信号。
如果父进程希望被告知其子系统的这种状态，则应捕捉此信号。
信号的捕捉函数中通常调用wait函数以取得进程ID和其终止状态。


os.wait函数用于等待子进程结束(只适用于UNIX兼容系统)。该函数返回包含两个元素的元组，包括已完成的子进程号pid
，以及子进程的退出状态，返回状态为0，表明子进程成功完成。返回状态为正整数表明子进程终止时出错。如没有子进程，会引发OSError错误。
os.wait要求父进程等待它的任何一个子进程结束执行，然后唤醒父进程。

要指示父进程等候一个指定的子进程终止，可在父进程中使用os.waitpid函数(只适用于unix兼容系统)。
它可等候一个指定进程结束，然后返回一个双元素元组，其中包括子进程的pid和子进程的退出状态。
函数调用将pid作为第一个参数传递，并将一个选项作为第二个选项，如果第一个参数大于0，
则waitpid会等待该pid结束，如果第一个参数是-1，则会等候所有子进程，也就和os.wait一样。
'''

print "Before the fork ,my pid is ",os.getpid()

pid =os.fork()

if pid:
    print "hello from the parent ,the child will be pid %d",pid
    print "sleeping 10s"
    time.sleep(10)
    print "sleep done"


else:
    print "child sleeping 5s"
    time.sleep(5)