# -*- coding: utf-8 -*-


class Student(object):
    def __init__(self, name):
        self.name = name

    # __str__()返回用户看到的字符串，而__repr__()返回开发者看到的字符串

    def __str__(self):
        return 'Student Object name {name: %s}' % self.name

    __repr__ = __str__


s = Student("bob")
print(s)

