# -*- coding: utf-8 -*-
from collections import Iterable

dict = {'a': 1, 'b': 2, 'c': 3}

# 迭代key
for key in dict:
    print(key)

# 迭代value
for value in dict.values():
    print(value)

# 迭代key & value
for key1, value1 in dict.items():
    print('key:', key1, 'value:', value1)

# 检测是否是可迭代对象

print(isinstance('string', Iterable))  # True

print(isinstance([1, 2, 3, 4], Iterable))  # True

print(isinstance(123, Iterable))  # False

print(isinstance((1, 2, 3, 4), Iterable))  # True

# 循环索引-元素对

for key, value in enumerate(['A', 'B', 'C']):
    print(key, value)
