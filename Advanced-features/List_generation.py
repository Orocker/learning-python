# -*- coding: utf-8 -*-
import os
#列表生成式

#生成list
list(range(1,11))

#生成[1x1,2x2,...,10x10] 平方list

list = []
for x in range(1,11):
	list.append(x * x)

print(list)

#更简单的写法

print([x * x for x in range(1,11)])

#只生成偶数平方

even_list = [x * x for x in range(1,11) if x % 2 == 0]
print(even_list)

#生成两层循环list

two_list = [m + n for m in 'ABC' for n in 'XYZ']
print(two_list)

#列出当前目录下所有文件和目录名
filename = [file for file in os.listdir('.')]
print(filename)

#for循环同时迭代key和value
dict = {'a':'A','b':'B','c':'C'}
for key,value in dict.items():
	print(key,'=',value)

#用两个变量生成list
equally_list = [key + '=' + value for key,value in dict.items()]
print(equally_list)

#把所有list字符串变成小写
word = ['2018','World','cup','Russia']
lower_word = [s.lower() for s in word]
print(lower_word)