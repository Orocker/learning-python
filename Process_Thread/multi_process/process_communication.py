# -*- coding: utf-8 -*-
from multiprocessing import Queue, Process
import os, time, random


# 以Queue为例，在父进程中创建两个子进程，一个往Queue里写数据，一个从Queue里读数据：

# 写数据进程执行的代码


def write(q):
    print("Process to write: %s" % os.getppid())
    for value in ['A', 'B', 'C']:
        print("put %s to queue..." % value)
        q.put(value)
        time.sleep(random.random())


def read(q):
    print("Process to read: %s" % os.getppid())
    while True:
        value = q.get(True)
        print("Get %s from queue." % value)


if __name__ == '__main__':
    q = Queue()  # 父进程创建Queue，并传给各个子进程：
    pw = Process(target=write, args=(q,))
    pr = Process(target=read, args=(q,))
    pw.start()  # 启动子进程pw，写入:
    pr.start()  # 启动子进程pw，读取
    pw.join()  # 等待pw结束
    pr.terminate()  # pr进程里是死循环，无法等待其结束，只能强行终止:

#  运行结果
# Process to write: 1148
# put A to queue...
# Process to read: 1148
# Get A from queue.
# put B to queue...
# Get B from queue.
# put C to queue...
# Get C from queue
