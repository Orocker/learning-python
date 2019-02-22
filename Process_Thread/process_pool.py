# -*- coding: utf-8 -*-
from multiprocessing import Pool
import os, time, random


# 如果要启动大量的子进程，可以用进程池的方式批量创建子进程：

def long_time_task(name):
    print("Run task %s (%s)" % (name, os.getppid()))
    start = time.time()
    time.sleep(random.random() * 3)
    end = time.time()
    print("Task %s runs %.3f seconds." % (name, (end - start)))


if __name__ == '__main__':
    print("Parent process %s." % os.getppid())
    p = Pool(4)
    for i in range(5):
        p.apply_async(long_time_task, args=(i,))
    print("Waiting for all subprocess done...")
    p.close()
    p.join()
    print("All subprocess done.")
