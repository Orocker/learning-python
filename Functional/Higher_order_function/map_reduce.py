# -*- coding: utf-8 -*-
from functools import reduce
#高阶函数 
#map 
def power(x):
	return x * x
r = map(power,[1,2,3,4,5,6,7,8,9,10])
list(r)#[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
list(map(str, [1, 2, 3, 4, 5, 6, 7, 8, 9])) #['1', '2', '3', '4', '5', '6', '7', '8', '9']

#map()传入的第一个参数是f，即函数对象本身。由于结果r是一个Iterator，Iterator是惰性序列，因此通过list()函数让它把整个序列都计算出来并返回一个list。

#reduce

def add(x,y):
	return x + y

reduce(add,[1,3,5,7,9])

#把列表元素变为连续的数字

def fn(x,y):
	return x*10+y

reduce(fn,[1,3,5,7,9])

#把str转为int

def str2num(s):
	 digits = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
	 return digits[s]

reduce(fn,map(str2num,'13579'))

#整理成一个函数
digits = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}

def str2int(s):
    def fn(x, y):
        return x * 10 + y
    def char2num(s):
        return digits[s]
    return reduce(fn, map(char2num, s))

#用lambda 整理
def char2num(s):
    return DIGITS[s]

def str2int(s):
    return reduce(lambda x, y: x * 10 + y, map(char2num, s))

#假设用户输入的英文名字不规范，没有按照首字母大写，后续字母小写的规则，请利用map()函数，把一个list（包含若干不规范的英文名字）变成一个包含规范英文名字的list
def format_name(s):
    return s[0].upper() + s[1:].lower()

print map(format_name, ['adam', 'LISA', 'barT'])

#求乘积
def prod(x, y):
    return x*y

print reduce(prod, [2, 4, 5, 7, 12])



