# -*- coding: utf-8 -*-

#匿名函数
#在Python中，对匿名函数提供了有限支持。还是以map()函数为例，计算f(x)=x^2时，除了定义一个f(x)的函数外，还可以直接传入匿名函数：

list(map(lambda x: x * x,range(10)))
#[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

lambda x: x* x 
#等于
def f(x):
	return x * x

#匿名函数有个限制，就是只能有一个表达式，不用写return，返回值就是该表达式的结果

#用匿名函数有个好处，因为函数没有名字，不必担心函数名冲突。此外，匿名函数也是一个函数对象，也可以把匿名函数赋值给一个变量，再利用变量来调用该函数：
# >>> f = lambda x: x * x
# >>> f
# <function <lambda> at 0x01E387C8>
# >>> f(5)
# 25

#也可以把匿名函数作为返回值返回，比如：
def build(x,y):
	return lambda: x * x + y * y
# >>> build(4,5)
# <function build.<locals>.<lambda> at 0x01E388E8>
# >>> f = build(4,5)
# >>> f()
# 41
# >>>
L = list(filter(lambda n: n % 2 == 1, range(1, 20)))
#[1, 3, 5, 7, 9, 11, 13, 15, 17, 19]

