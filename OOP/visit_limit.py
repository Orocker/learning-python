# -*- coding: utf-8 -*-

class Student(object):

    # 属性名称前加 __ 表示这个属性为私有属性 变量前面加 __ 表示为私有变量
    # 私有属性、私有变量外部无法访问

    def __init__(self, name, score):
        self.__name = name
        self.__score = score

    def get_name(self):
        return self.__name

    def get_score(self):
        return self.__score

    def set_score(self, score):
        if 0 <= score <= 100:
            self.__score = score
        else:
            raise ValueError('bad score')

    def get_grade(self):
        if self.__score >= 90:
            return 'A'
        elif self.__score >= 60:
            return 'B'
        else:
            return 'C'


class Student1(object):
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender

    def set_gender(self, gender):
        if gender == 'male' or gender == 'fmale':
            self.__gender = gender
        else:
            raise ValueError('Bad Value')

    def get_gender(self, gender):
        return self.__gender


bart = Student('Bart Simpson', 59)
print('bart.get_name() =', bart.get_name())
bart.set_score(60)
print('bart.get_score() =', bart.get_score())

print('DO NOT use bart._Student__name:', bart._Student__name)
