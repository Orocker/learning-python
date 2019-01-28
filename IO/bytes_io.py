# -*- coding: utf-8 -*-
from io import BytesIO

# StringIO操作的只能是str，如果要操作二进制数据，就需要使用BytesIO。
# BytesIO实现了在内存中读写bytes，下面先创建一个BytesIO，然后写入一些bytes：

f = BytesIO()

f.write("你好".encode('utf-8'))  # 6 请注意，写入的不是str，而是经过UTF-8编码的bytes。

print(f.getvalue())  # b'\xe4\xbd\xa0\xe5\xa5\xbd'

# 和StringIO类似，可以用一个bytes初始化BytesIO，然后，像读文件一样读取：

b = BytesIO(b'\xe4\xbd\xa0\xe5\xa5\xbd')
print(b.read()) # b'\xe4\xbd\xa0\xe5\xa5\xbd'
