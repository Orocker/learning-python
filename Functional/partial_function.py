# -*- coding: utf-8 -*-
int('12')  # 12
int('1000000', base=2)  # base转换成对应的N进制，默认10进制


def int2(x, base=2):
    return int(x, base)


# 偏函数

import functools

fint2 = functools.partial(int, base=2)
fint2('1000000')  # 64
fint2('100000', base=10)  # 100000
# functools.partial的作用就是，把一个函数的某些参数给固定住（也就是设置默认值），返回一个新的函数，调用这个新函数会更简单。
