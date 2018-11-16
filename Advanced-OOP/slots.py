# -*- coding: utf-8 -*-


class Student(object):
    pass


s = Student()


# 给实例绑定属性
# s.name = 'Material'
# print(s.name)  #Material

# 给实例绑定方法


def set_age(self, age):
    self.age = age


from types import MethodType

s.set_age = MethodType(set_age, s)
s.set_age(26)
print(s.age)  # 26
# 给一个实例绑定的方法，对另一个实例不起作用
# s2 = Student()
# print(s2.set_age(28))


def set_score(self, score):
    self.score = score


Student.set_score = set_score  # 给类绑定方法，所有实例都可以用这个方法
s2 = Student()
s2.set_score(50)
s.set_score(30)
print(s.score)  # 50
print(s2.score)  # 30

# __slots__ 用法
# __slots__定义的属性仅对当前类实例起作用，对继承的子类是不起作用的：
# 除非在子类中也定义__slots__，这样，子类实例允许定义的属性就是自身的__slots__加上父类的__slots__


class Father(object):
    __slots__ = ('name', 'age')


f = Father()
f.name = 'Grace'
f.age = 50
# f.score = 80  由于'score'没有被放到__slots__中，所以不能绑定score属性，试图绑定score将得到AttributeError的错误

print(f.name, f.age)


class Son(Father):
    __slots__ = ('school', 'job')


son = Son()
# son.score = 50  # AttributeError: 'Son' object has no attribute 'score'




