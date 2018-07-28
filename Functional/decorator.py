# -*- coding: utf-8 -*-

import math


# 三个函数，对执行的函数打印调用日志

def f1(x):
	print("call f1")
	return x *2

def f2(x):
	print("call f2")
	return x * x

def f3(x):
	print("call f3")
	return x * x * x

#装饰器函数

def new_fn(f):
	def fn(x):
		print('call'+ fn.__name__+ '()')
		return f(x)
	return fn