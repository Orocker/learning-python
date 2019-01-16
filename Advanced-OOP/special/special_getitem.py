# -*- coding: utf-8 -*-


# __getitem
# Fib实例虽然能作用于for循环，看起来和list有点像，但是，把它当成list来使用还是不行，比如，取第5个元素：
# 要表现得像list那样按照下标取出元素，需要实现__getitem__()方法：


class Fib(object):
    def __getitem__(self, n):
        a, b = 1, 1
        for x in range(n):
            a, b = b, a + b
        return a


f1 = Fib()
print(f1[0], f1[1], f1[2], f1[100])

# list有个切片的方法


list1 = list(range(100))[5:20]
print("list1:", list1)

f2 = Fib()


#  list2 = f2[0:5]  这样会报错，原因是__getitem__()传入的参数可能是一个int，也可能是一个切片对象slice，所以要做判断


class Fib1(object):
    def __getitem__(self, n):
        if isinstance(n, int):  # n是索引
            a, b = 1, 1
            for x in range(n):
                a, b = b, a + b
            return a
        if isinstance(n, slice):  # n是切片
            start = n.start
            stop = n.stop
            if start is None:
                start = 0
            a, b = 1, 1
            L = []
            for x in range(stop):
                if x >= start:
                    L.append(a)
                a, b = b, a + b
            return L


f3 = Fib1()
list3 = f3[:5]
print("list3:", list3)

# 但是没有对 step 和负数做处理
# 此外，如果把对象看成dict，__getitem__()的参数也可能是一个可以作key的object，例如str。
# 与之对应的是__setitem__()方法，把对象视作list或dict来对集合赋值。最后，还有一个__delitem__()方法，用于删除某个元素。
# 通过上面的方法，我们自己定义的类表现得和Python自带的list、tuple、dict没什么区别，这完全归功于动态语言的“鸭子类型”，不需要强制继承某个接口。


list4 = f3[:5:2]
print("list4:", list4)
