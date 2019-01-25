# -*- coding: utf-8 -*-

# 写文件
# 写文件和读文件是一样的，唯一区别是调用open()函数时，传入标识符'w'或者'wb'表示写文本文件或写二进制文件：
w = open('file/write.txt', 'w')
w.write('Hello! ')
w.close()

# 可以反复调用write()来写入文件，但是务必要调用w.close()来关闭文件。当写文件时，操作系统往往不会立刻把数据写入磁盘，而是放到内存缓存起来，空闲的时候再慢慢写入。
# 只有调用close()方法时，操作系统才保证把没有写入的数据全部写入磁盘。忘记调用close()的后果是数据可能只写了一部分到磁盘，剩下的丢失了。所以，还是用with语句来得保险：
# 以追加的方式写入用 'a'

with open('file/write.txt', 'a') as w:
    w.write('Hello for write')

# 要写入特定编码的文本文件，请给open()函数传入encoding参数，将字符串自动转换成指定编码。
