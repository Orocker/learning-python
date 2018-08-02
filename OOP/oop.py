#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#面向过程
#数据封装、继承和多态是面向对象的三大特点
std1 = { 'name': 'Michael', 'score': 98 }
std2 = { 'name': 'Bob', 'score': 81 }

def print_score(std):
	print('%s: %s' % (std['name'], std['score']))

#面向对象

class Student(object):
	"""docstring for Student"""
	def __init__(self, name,score):
		self.name = name
		self.score = score

	def print_score(self):
		print('%s: %s' % (self.name, self.score))

bart = Student('Bob',20)
lisa = Student('Lisa Simpson', 87)
bart.print_score()
lisa.print_score()