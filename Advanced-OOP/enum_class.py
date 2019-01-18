# -*- coding: utf-8 -*-
from enum import Enum, unique

# 当我们需要定义常量时，一个办法是用大写变量通过整数来定义，例如月份：
# 它的好处是简单，缺点是类型是int，并且仍然是变量。

JAN = 1
FEB = 2
MAR = 3

print(JAN, FEB, MAR)

# 更好的方法是为这样的枚举类型定义一个class类型，然后，每个常量都是class的一个唯一实例。Python提供了Enum类来实现这个功能：
Month = Enum('Month', ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))

# 这样我们就获得了Month类型的枚举类，可以直接使用Month.Jan来引用一个常量，或者枚举它的所有成员：
# value属性则是自动赋给成员的int常量，默认从1开始计数。
for name, member in Month.__members__.items():
    print(name, '=>', member, ':', member.value)

    # Output
    # Jan = > Month.Jan: 1
    # Feb = > Month.Feb: 2
    # Mar = > Month.Mar: 3
    # Apr = > Month.Apr: 4
    # May = > Month.May: 5
    # Jun = > Month.Jun: 6
    # Jul = > Month.Jul: 7
    # Aug = > Month.Aug: 8
    # Sep = > Month.Sep: 9
    # Oct = > Month.Oct: 10
    # Nov = > Month.Nov: 11
    # Dec = > Month.Dec: 12


# 如果需要更精确地控制枚举类型，可以从Enum派生出自定义类：


@unique
class Weekday(Enum):
    Sun = 0
    Mon = 1
    Tue = 2
    Wed = 3
    Thu = 4
    Fri = 5
    Sat = 6


# 访问这些枚举类型可以有若干种方法： 既可以用成员名称引用枚举常量，又可以直接根据value的值获得枚举常量。

day1 = Weekday.Mon
print('day1:', day1)  # day1: Weekday.Mon
print(Weekday.Tue)  # Weekday.Tue
print(Weekday['Tue'])  # Weekday.Tue
print(Weekday.Tue.value)  # 2
print(day1 == Weekday.Mon)  # True
print(day1 == Weekday.Tue)  # False
print(Weekday(1))  # Weekday.Mon
print(day1 == Weekday(1))  # True
# print(Weekday(7))  # Traceback (most recent call last):

for name, member in Weekday.__members__.items():
    print(name, '=>', member)

Gender = Enum('Gender', ('Male', 'Female'))


class Student(object):
    def __init__(self, names, gender):
        self.name = names
        self.gender = gender


bart = Student('Bart', Gender.Male)
if bart.gender == Gender.Male:
    print('SUCCESS!')
else:
    print('FAILED!')
