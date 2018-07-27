# -*- coding: utf-8 -*-

#高阶函数
"""
函数本身也可以赋值给变量，即：变量可以指向函数
函数名也是变量
传入函数

"""
def add(x, y, f):
    return f(x) + f(y)

add(-5, 6, abs) #11

#推导计算过程为
# x = -5
# y = 6
# f = abs
# f(x) + f(y) ==> abs(-5) + abs(6) ==> 11
# return 11
