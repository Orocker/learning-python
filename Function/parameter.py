# -*- coding: utf-8 -*-
import math


# 求平方
def power(x):
    if not isinstance(x, (int, float)):
        raise TypeError('Bad operand type')
    else:
        return x * x


power(5)


# 求一个数的N次方
def powerN(x, n):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s


powerN(5, 5)


# 默认参数	 默认参数必须指向不变对象！
def powerD(x, n=2):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s


powerD(5)
powerD(5, 10)


def add_end(list=None):
    if list is None:
        list = []
    list.append('END')


# 可变参数
# 在Python函数中。可变参数就是传入的参数个数是可变的，可以是1个、2个到任意个，还可以是0个。
# 求一个list所有元素平方的和

def calc(numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum


calc([1, 3, 5, 7, 9])


# 改为可变参数

def calc1(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum


calc1(1, 3, 5, 7, 9)
# 不传参数返回0
calc1()
# 调用已有的list 或 tuple

list1 = [1, 2, 3, 4, 5]
calc1(*list1)


# 关键字参数
# 关键字参数允许你传入0个或任意个含参数名的参数，这些关键字参数在函数内部自动组装为一个dict。
# 对于关键字参数，函数的调用者可以传入任意不受限制的关键字参数。至于到底传入了哪些，就需要在函数内部通过kw检查。

def person(name, age, **kw):
    print('name:', name, 'age:', age, 'other:', kw)


person('Michael', 30)
person('Bob', 35, city='Beijing')
# 组装字典传入关键字参数
# **extra表示把extra这个dict的所有key-value用关键字参数传入到函数的**kw参数，kw将获得一个dict，注意kw获得的dict是extra的一份拷贝，对kw的改动不会影响到函数外的extra。
extra = {'city': 'Beijing', 'job': 'Engineer'}
person('Jack', 24, **extra)


# 命名关键字参数

# 限制关键字参数的名字，就可以用命名关键字参数，例如，只接收city和job作为关键字参数。
# 和关键字参数**kw不同，命名关键字参数需要一个特殊分隔符*，*后面的参数被视为命名关键字参数。
def person(name, age, *, city, job):
    print(name, age, city, job)


person('Jack', 24, city='Beijing', job='Engineer')


# 如果函数定义中已经有了一个可变参数，后面跟着的命名关键字参数就不再需要一个特殊分隔符*了，命名关键字参数必须传入参数名
def person(name, age, *args, city, job):
    print(name, age, args, city, job)


# 命名关键字参数可以有缺省值，从而简化调用
def person(name, age, *, city='Beijing', job):
    print(name, age, city, job)


person('Jack', 24, job='Engineer')

# 参数组合
"""
在Python中定义函数，可以用必选参数、默认参数、可变参数、关键字参数和命名关键字参数，这5种参数都可以组合使用。但是请注意，参数定义的顺序必须是：必选参数、默认参数、可变参数、命名关键字参数和关键字参数。
"""


# 比如定义一个函数，包含上述若干种参数：

def f1(a, b, c=0, *args, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'args =', args, 'kw =', kw)


def f2(a, b, c=0, *, d, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'd =', d, 'kw =', kw)


# 在函数调用的时候，Python解释器自动按照参数位置和参数名把对应的参数传进去。

f1(1, 2)
# a = 1 b = 2 c = 0 args = () kw = {}
f1(1, 2, c=3)
# a = 1 b = 2 c = 3 args = () kw = {}
f1(1, 2, 3, 'a', 'b')
# a = 1 b = 2 c = 3 args = ('a', 'b') kw = {}
f1(1, 2, 3, 'a', 'b', x=99)
# a = 1 b = 2 c = 3 args = ('a', 'b') kw = {'x': 99}
f2(1, 2, d=99, ext=None)
# a = 1 b = 2 c = 0 d = 99 kw = {'ext': None}
# 最神奇的是通过一个tuple和dict，你也可以调用上述函数：

args = (1, 2, 3, 4)
# kw = {'d': 99, 'x': '#'}
f1(*args, **kw)
# a = 1 b = 2 c = 3 args = (4,) kw = {'d': 99, 'x': '#'}
args = (1, 2, 3)
kw = {'d': 88, 'x': '#'}
f2(*args, **kw)
# a = 1 b = 2 c = 3 d = 88 kw = {'x': '#'}
