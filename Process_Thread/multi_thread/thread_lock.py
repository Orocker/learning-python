# -*- coding: utf-8 -*-
import time,threading

# 针对thread_no_lock.py的问题，要确保balance计算正确，就要给change_it()上一把锁，当某个线程开始执行change_it()时，可以说，该线程因为获得了锁，
# 因此其他线程不能同时执行change_it()，只能等待，直到锁被释放后，获得该锁以后才能改。由于锁只有一个，
# 无论多少线程，同一时刻最多只有一个线程持有该锁，所以，不会造成修改的冲突。创建一个锁就是通过threading.Lock()来实现：

balance = 0
lock = threading.Lock()


def change_it(n):
    global balance
    balance = balance + n
    balance = balance - n


def run_thread(n):
    for i in range(100000):
        # 先获取锁
        lock.acquire()
        try:
            # 修改数据
            change_it(n)
        finally:
            # 修改完后释放锁
            lock.release()


t1 = threading.Thread(target=run_thread, args=(5,))
t2 = threading.Thread(target=run_thread, args=(8,))
t1.start()
t2.start()
t1.join()
t2.join()
print(balance)

# 注意
# 当多个线程同时执行lock.acquire()时，只有一个线程能成功地获取锁，然后继续执行代码，其他线程就继续等待直到获得锁为止。
# 获得锁的线程用完后一定要释放锁，否则其他线程将永远等待下去，成为死线程。所以用try...finally来确保锁一定会被释放。
