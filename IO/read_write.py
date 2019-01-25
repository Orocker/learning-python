# -*- coding: utf-8 -*-

# 以读方式打开文件，如果打开不存在的文件，open()函数就会抛出一个IOError的错误，并且给出错误码和详细的信息告诉你文件不存在

# f = open('file/text.txt', 'r')
# print(f.read())
# f.close()


# 由于文件读写时都有可能产生IOError，一旦出错，后面的f.close()就不会调用。所以，为了保证无论是否出错都能正确地关闭文件，我们可以使用try ... finally来实现：

# try:
#     f = open('file/text.txt', 'r')
#     print(f.read())
# finally:
#     if f:
#         f.close()


# 但是每次都这么写实在太繁琐，所以，Python引入了with语句来自动帮我们调用close()方法：这和try ... finally是一样的，但是代码更佳简洁，并且不必调用f.close()方法。

with open('file/text.txt', 'r') as f:
    print(f.read())

