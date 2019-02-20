# -*- coding: utf-8 -*-
import pickle

d = dict(name='Bob', age=20, score=88)
# pickle.dumps()方法把任意对象序列化成一个bytes，然后，就可以把这个bytes写入文件。或者用另一个方法pickle.dump()直接把对象序列化后写入一个file-like Object：
s = pickle.dumps(d)
print(s)

f = open('file/pickling.txt', 'wb')

pickle.dump(d, f)  # 文件保存的都是Python保存的对象内部信息

#  当我们要把对象从磁盘读到内存时，可以先把内容读到一个bytes，然后用pickle.loads()方法反序列化出对象，
#  也可以直接用pickle.load()方法从一个file-like Object中直接反序列化出对象。我们打开另一个Python命令行来反序列化刚才保存的对象
f1 = open('file/pickling.txt', 'rb')
d1 = pickle.load(f1)
f1.close()
print(d1)  # {'name': 'Bob', 'age': 20, 'score': 88} 这个变量和原来的变量是完全不相干的对象，它们只是内容相同而已。
