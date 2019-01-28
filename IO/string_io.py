# -*- coding: utf-8 -*-
from io import StringIO

# 很多时候，数据读写不一定是文件，也可以在内存中读写。
# StringIO就是在内存中读写str。
# 要把str写入StringIO，需要先创建一个StringIO，然后像文件一样写入即可：

f = StringIO()
f.write('Hello')  # 5
f.write(' ')  # 1
f.write('for python')  # 10
print(f.getvalue())  # Hello for python :getvalue()方法用于获得写入后的str。


# 要读取StringIO，可以用一个str初始化StringIO，然后，像读文件一样读取：

r = StringIO("Hello\nfor\nPython\n")
while True:
    s = r.readline()
    if s == '':
        break
    print(s.strip())

# Hello
# for
# Python
