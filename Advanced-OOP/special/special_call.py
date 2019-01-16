# -*- coding: utf-8 -*-


# 一个对象实例可以有自己的属性和方法，当调用实例方法时，用instance.method()来调用。能不能直接在实例本身上调用呢？在Python中，答案是肯定的。
# 任何类，只需要定义一个__call__()方法，就可以直接对实例进行调用。
class Student(object):
    def __init__(self, name):
        self.name = name

    def __call__(self):
        print('My name is %s.' % self.name)


s = Student('Michel')
print(s())

# __call__()还可以定义参数
# 需要判断一个对象是否能被调用，能被调用的对象就是一个Callable对象，比如函数和我们上面定义的带有__call__()的类实例
# 通过callable()函数，我们就可以判断一个对象是否是“可调用”对象。

print(callable(Student('test')))  # True
