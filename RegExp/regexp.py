# -*- coding: utf-8 -*-
import re

# Python提供re模块，包含所有正则表达式的功能。由于Python的字符串本身也用\转义，所以要特别注意
# 因此强烈建议使用Python的r前缀，就不用考虑转义的问题了：
mobile = "010-12345"
# match()方法判断是否匹配，如果匹配成功，返回一个Match对象，否则返回None
s = re.match(r'^\d{3}\-\d{3,8}$', mobile)
# 常见的判断是否匹配方法

if re.match(r'^\d{3}\-\d{3,8}$', mobile):
    print("Matched")
else:
    print("Match Failed")

# 切割字符串
print('a b   c'.split(' '))  # 普通切割，无法识别连续的空格 ['a', 'b', '', '', 'c']
print(re.split(r'\s+', 'a b   c'))  # 正则切割，无论多少个空格都可以正常分割 ['a', 'b', 'c']
print(re.split(r'[\s\,]+', 'a,b, c  d'))  # ['a', 'b', 'c', 'd']
print(re.split(r'[\s\,\;]+', 'a,b;; c  d'))  # ['a', 'b', 'c', 'd']

# 分组 正则表达式有提取子串的强大功能。用()表示的就是要提取的分组（Group）

m = re.match(r'^(\d{3})\-(\d{3,8})', '010-12345')
# 如果正则表达式中定义了组，就可以在Match对象上用group()方法提取出子串来。
# group(0)永远是原始字符串，group(1)、group(2)……表示第1、2、……个子串。
print(m.group(0))  # 010-12345
print(m.group(1))  # 010
print(m.group(2))  # 12345

# 匹配时间
t = '19:05:30'
reg_t = re.match(
    r'^(0[0-9]|1[0-9]|2[0-3]|[0-9])\:(0[0-9]|1[0-9]|2[0-9]|3[0-9]|4[0-9]|5[0-9]|[0-9])\:(0[0-9]|1[0-9]|2[0-9]|3[0-9]|4[0-9]|5[0-9]|[0-9])$',
    t)
print(reg_t.group(0))  # 19:05:30

date = '2-31'
reg_date = re.match(r'^(0[1-9]|1[0-2]|[0-9])-(0[1-9]|1[0-9]|2[0-9]|3[0-1]|[0-9])$', date)
print(reg_date.groups())

# 贪婪匹配
# 正则匹配默认是贪婪匹配，也就是匹配尽可能多的字符

greedy = re.match(r'^(\d+)(0*)$', '102300').groups()
print(greedy)  # ('102300', '') 由于\d+采用贪婪匹配，直接把后面的0全部匹配了，结果0*只能匹配空字符串了。

print(re.match(r'^(\d+?)(0*)$', '102300').groups()) # ('1023', '00')
