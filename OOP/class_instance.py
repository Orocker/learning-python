# -*- coding: utf-8 -*-

#定义类
class Student(object):
	"""docstring for Student"""
	#类的特殊方法，在创建实例的时候，把属性绑定上去，self表示实例本身
	#
	def __init__(self,name,score):
		self.name = name
		self.score = score

	#和普通的函数相比，在类中定义的函数只有一点不同，就是第一个参数永远是实例变量self，并且，调用时，不用传递该参数。除此之外，类的方法和普通函数没有什么区别
	def print_score(self):
        print('%s: %s' % (self.name, self.score))

    def get_grade(self):
        if self.score >= 90:
            return 'A'
        elif self.score >= 60:
            return 'B'
        else:
            return 'C'

#类的实例
bart = Student() #<__main__.Student object at 0x0034EDD0>
Student  #<class '__main__.Student'>

#类绑定属性
s.name = 'lily'
s.name #'lily'
		