# -*- coding: utf-8 -*-
from collections import Iterator

# 判断是否是迭代器(Iterator)
isinstance((x for x in range(10)), Iterator)  # True

isinstance([], Iterator)  # False

isinstance({}, Iterator)  # False

isinstance('abc', Iterator)  # False

"""
生成器都是Iterator对象，但list、dict、str虽然是Iterable，却不是Iterator。
把list、dict、str等Iterable变成Iterator可以使用iter()函数
"""

isinstance(iter([]), Iterator)  # True
isinstance(iter('abc'), Iterator)  # True

"""
凡是可作用于for循环的对象都是Iterable类型；
凡是可作用于next()函数的对象都是Iterator类型,它们表示一个惰性计算的序列
集合数据类型如list、dict、str等是Iterable但不是Iterator，不过可以通过iter()函数获得一个Iterator对象。
Python的for循环本质上就是通过不断调用next()函数实现的
"""
for x in [1, 2, 3, 4, 5]:
    pass
# 等价于

it = iter([1, 2, 3, 4, 5])
# 循环:
while True:
    try:
        # 获得下一个值:
        x = next(it)
    except StopIteration:
        # 遇到StopIteration就退出循环
        break
