# -*- coding: utf-8 -*-
import math

def move(x,y,step,angle=0):
    nx = x+step * math.cos(angle)
    ny = y+step * math.sin(angle)
    return nx,ny
x,y = move(100, 100, 60, math.pi / 6)
print(x,y)

def power(x):
    return x * x
print(power(20))