# -*- coding: utf-8 -*-
import math


# 用filter函数只保留列表中的奇数
def is_odd(n):
    return n % 2 == 1


r = list(filter(is_odd, [1, 2, 4, 5, 6, 9, 10, 15]))
print(r)


# 用filter函数删除序列中的空字符串

def not_empty(s):
    return s and s.strip()


r1 = list(filter(not_empty, ['A', '', 'B', None, 'C', '  ']))
r2 = filter(not_empty, ['A', '', 'B', None, 'C',
                        '  '])  # 到filter()函数返回的是一个Iterator，也就是一个惰性序列，所以要强迫filter()完成计算结果，需要用list()函数获得所有结果并返回list。
print(r1)
print(r2)


# 用filter求素数()

# 从3开始的奇数序列
def _odd_iter():
    n = 1
    while True:
        n = n + 2
        yield n


# 定义筛选函数
def _not_divisible(n):
    return lambda x: x % n > 0


def primes():
    yield 2
    it = _odd_iter()
    while True:
        n = next(it)
        yield n
        it = filter(_not_divisible(n), it)


for n in primes():
    if n < 1000:
        print(n)
    else:
        break


# 用filter筛选回数
def is_palindrome(n):
    return str(n) == str(n)[::-1]


output = filter(is_palindrome, range(1, 1000))
print(list(output))
