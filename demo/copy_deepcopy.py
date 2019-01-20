# -*- coding: utf-8 -*-
import copy

a = [1, 2, 3]
b = a
print(id(a))  # 2835880
print(id(b))  # 2835880

b[0] = 11

print(id(a) == id(b))  # True

c = copy.copy(a)

print(id(c) == id(a))  # False

c[1] = 22
print(c)  # 只有c会改变

a1 = [1, 2, [3, 4]]
d = copy.copy(a1)  # 不完全Copy，相同的部分会跟着被改变

# >>> f = [1,2,[3,4]]
# >>> f
# [1, 2, [3, 4]]
# >>> g = copy.copy(f)
# >>> g
# [1, 2, [3, 4]]
# >>> f[2][0] =88
# >>> f
# [1, 2, [88, 4]]
# >>> g
# [1, 2, [88, 4]]
print(id(a1) == id(d))  # False

print(id(a1[2]) == id(d[2]))  # True

e = copy.deepcopy(a1)

print(id(a1) == id(e))  # False DeepCopy 完全Copy 内存空间不等

print(id(e[2]) == id(a1[2]))  # False

# ‘’=‘’   前后是同一个对象
# a = copy.copy(x）   只是复制的第一层，其余层是同一个对象
# a = copy.deepcopy(x)   把所有层都复制了一遍，属于不同的对象﻿
