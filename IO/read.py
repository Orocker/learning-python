# -*- coding: utf-8 -*-

# 以读方式打开文件，如果打开不存在的文件，open()函数就会抛出一个IOError的错误，并且给出错误码和详细的信息告诉你文件不存在

f = open('file/text.txt', 'r')
print(f.read())
f.close()


# 由于文件读写时都有可能产生IOError，一旦出错，后面的f.close()就不会调用。所以，为了保证无论是否出错都能正确地关闭文件，我们可以使用try ... finally来实现：

try:
    f = open('file/text.txt', 'r')
    print(f.read())
finally:
    if f:
        f.close()


# 但是每次都这么写实在太繁琐，所以，Python引入了with语句来自动调用close()方法：这和try ... finally是一样的，但是代码更佳简洁，并且不必调用f.close()方法。

with open('file/text.txt', 'r') as f:
    print(f.read())


# 调用read()会一次性读取文件的全部内容，如果文件有10G，内存就爆了，所以，要保险起见，可以反复调用read(size)方法，
# 每次最多读取size个字节的内容。另外，调用readline()可以每次读取一行内容，调用readlines()一次读取所有内容并按行返回list。因此，要根据需要决定怎么调用。
# 如果文件很小，read()一次性读取最方便；如果不能确定文件大小，反复调用read(size)比较保险；如果是配置文件，调用readlines()最方便：

f = open('file/text.txt', 'r')
for line in f.readlines():
    print(line.strip())  # # 把末尾的'\n'删掉

# file-like Object

# 像open()函数返回的这种有个read()方法的对象，在Python中统称为file-like Object。除了file外，还可以是内存的字节流，网络流，自定义流等等。
# file-like Object不要求从特定类继承，只要写个read()方法就行。StringIO就是在内存中创建的file-like Object，常用作临时缓冲。


# 二进制文件
# 读取二进制文件，比如图片、视频等等，用'rb'模式打开文件即可：

fb = open('file/images/bliss.jpg', 'rb')
print(fb.read())

# 字符编码
# 要读取非UTF-8编码的文本文件，需要给open()函数传入encoding参数，例如，读取GBK编码的文件：

gbk = open('file/gbk.txt', 'r', encoding='gbk')
print(gbk.read())

# 遇到有些编码不规范的文件，你可能会遇到UnicodeDecodeError，因为在文本文件中可能夹杂了一些非法编码的字符。遇到这种情况，
# open()函数还接收一个errors参数，表示如果遇到编码错误后如何处理。最简单的方式是直接忽略

ignore_gbk = open('file/gbk.txt', 'r', encoding='gbk', errors='ignore')
print(ignore_gbk.read())