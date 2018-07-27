# -*- coding: utf-8 -*-
import math

#定义一个返回绝对值的函数
def my_abs(x):
	if x > 0:
		return x
	else:
		return -x

#定义一个返回绝对值的函数，对传入的参数类型检查
def abs1(x):
	if not isinstance(x,(int,float)):
		raise TypeError('Bad Operand Type') 
	if x > 0:
		return x
	else:
		return -x


#从一个点移动到另一个点，给出坐标、位移和角度，计算出新的新的坐标（返回一个tuple）
def move(x,y,step,angle=0):
    nx = x+step * math.cos(angle)
    ny = y+step * math.sin(angle)
    return nx,ny
x,y = move(100, 100, 60, math.pi / 6)
print(x,y)
