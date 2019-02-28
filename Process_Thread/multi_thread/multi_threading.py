# -*- coding: utf-8 -*-
import time,threading

# 启动一个线程就是把一个函数传入并创建Thread实例，然后调用start()开始执行：

# 新线程执行的代码:


def loop():
    print("Thread %s is running..." % threading.current_thread().name)
    n = 0
    while n < 5:
        n += 1
        print("thread %s  >>> %s " % (threading.current_thread().name, n))
        time.sleep(1)
    print("thread %s is ended " % threading.current_thread().name)

#  由于任何进程默认就会启动一个线程，该线程称为主线程(MainThread)，主线程又可以启动新的线程
#  Python的threading模块有个current_thread()函数，它永远返回当前线程的实例，主线程实例的名字叫MainThread，
#  子线程的名字在创建时指定,下面用 loopThread 命名子线程，名字仅仅在打印时用来显示，完全没有其他意义，如果不起名字Python就自动给线程命名为Thread-1，Thread-2……


if __name__ == '__main__':
    print("Thread %s is running..." % threading.current_thread().name)
    t = threading.Thread(target=loop, name='loopThread')
    t.start()
    t.join()
    print("thread %s is ended " % threading.current_thread().name)

