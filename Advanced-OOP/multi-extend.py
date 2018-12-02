# -*- coding: utf-8 -*-

# 功能类


class Runnable(object):
    def run(self):
        print('Running...')


class Flyable(object):
    def fly(self):
        print('flying...')

# 基类


class Animal(object):
    pass

# 大类


class Mammal(Animal):
    pass


class Bird(Animal):
    pass

# 动物实体类


class Dog(Mammal, Runnable):
    pass


class Bat(Animal, Flyable):
    pass


class Parrot(Bird):
    pass


class Ostrich(Mammal):
    pass


dog = Dog()
dog.run()

bat = Bat()
bat.fly()

