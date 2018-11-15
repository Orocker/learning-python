# -*- coding: utf-8 -*-
# 装饰器
import functools
from time import strftime, gmtime


# 设我们要增强now()函数的功能，比如，在函数调用前后自动打印日志，但又不希望修改now()函数的定义，这种在代码运行期间动态增加功能的方式，称之为“装饰器”（Decorator）。
# 本质上，decorator就是一个返回函数的高阶函数。所以，我们要定义一个能打印日志的decorator，可以定义如下：

def log(func):
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__)
        return func(*args, **kw)

    return wrapper


# @log == log(now)
@log
def now():
    print(strftime("%Y-%m-%d %H:%M:%S", gmtime()))


now()


def logs(text):
    def decorator(func):
        def wrapper(*args, **kw):
            print('function %s %s():' % (text, func.__name__))
            return func(*args, **kw)

        return wrapper

    return decorator


@logs('execute')
def nows():
    print(strftime("%Y-%m-%d %H:%M:%S", gmtime()))


nows()


# 三个函数，对执行的函数打印调用日志

def f1(x):
    print("call f1")
    return x * 2


def f2(x):
    print("call f2")
    return x * x


def f3(x):
    print("call f3")
    return x * x * x


# 改为装饰器函数

def new_fn(f):
    def fn(x):
        print('call' + fn.__name__ + '()')
        return f(x)

    return fn
