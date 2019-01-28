# -*- coding: utf-8 -*-
import os

print(os.name)

# windows不提供  Linux： ('Linux', 'grocker', '4.10.4-1.el7.elrepo.x86_64', '#1 SMP Sat Mar 18 12:50:10 EDT 2017', 'x86_64')
print(os.uname())

print(os.environ) # 获取环境变量

# 获取环境变量的某个值

print(os.environ.get('PATH'))


# 操作文件和目录

# 查看当前目录的绝对路径:
current_path = os.path.abspath('.')  # E:\py\learning-python

# 在某个目录下创建一个新目录，首先把新目录的完整路径表示出来:
new_path = os.path.join(current_path, 'new_dir') # E:\py\learning-python\new_dir

# 然后创建一个目录:
os.mkdir(new_path)

# 删除一个目录
os.rmdir(new_path)

# 把两个路径合成一个时，不要直接拼字符串，而要通过os.path.join()函数，
# 这样可以正确处理不同操作系统的路径分隔符。在Linux/Unix/Mac下，os.path.join()返回这样的字符串：
# Unix : part-1/part-2  Windows: part-1\part-2

# 拆分路径时，也不要直接去拆字符串，而要通过os.path.split()函数，这样可以把一个路径拆分为两部分，后一部分总是最后级别的目录或文件名：
split_path = os.path.split(current_path + "/Readme.md")
split_path1 = os.path.split(current_path)
print(split_path)  # ('E:\\py\\learning-python', 'Readme.md')
print(split_path1)  # ('E:\\py', 'learning-python')

# 获取文件扩展名
ext = os.path.splitext(current_path + "/Readme.md")
print(ext)  # ('E:\\py\\learning-python/Readme', '.md')

# 这些合并、拆分路径的函数并不要求目录和文件要真实存在，它们只对字符串进行操作。
# 文件操作使用下面的函数。假定当前目录下有一个test.txt文件：
# os.rename('test.txt', 'test.py')  # 重命名文件
# os.remove('test.py') # 删除文件

# 列出当前目录下的所有文件
[x for x in os.listdir('.') if os.path.isdir(x)] # ['file']

# 列出所有的.py文件
[x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1] == '.py']
# ['bytes_io.py', 'file_dir.py', 'read.py', 'string_io.py', 'write.py']
