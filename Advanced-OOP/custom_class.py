# -*- coding: utf-8 -*-


class Student(object):
    def __init__(self, name):
        self.name = name

# __str__()返回用户看到的字符串，而__repr__()返回开发者看到的字符串

    def __str__(self):
        return 'Student Object name {name: %s}' % self.name
    __repr__ = __str__

# __iter__ 如果一个类想被用于for ... in循环，类似list或tuple那样，就必须实现一个__iter__()方法，该方法返回一个迭代对象，
# 然后，Python的for循环就会不断调用该迭代对象的__next__()方法拿到循环的下一个值，直到遇到StopIteration错误时退出循环。


s = Student("bob")
print(s)


class Fib(object):
    def __init__(self):
        self.a, self.b = 0, 1  # 初始化两个计数器a，b

    def __iter__(self):
        return self  # 实例本身就是迭代对象，所以返回自己

    def __next__(self):
        self.a, self.b = self.b, self.a + self.b  # 计算下一个值
        if self.a > 100000:
            raise StopIteration
        return self.a   # 返回下一个值


for n in Fib():
    print(n)


# __getitem
# Fib实例虽然能作用于for循环，看起来和list有点像，但是，把它当成list来使用还是不行，比如，取第5个元素：