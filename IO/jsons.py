# -*- coding: utf-8 -*-
import json

#  Python内置的json模块提供了非常完善的Python对象到JSON格式的转换
# JSON类型	    Python类型
# {}	          dict
# []	          list
# "string"	  str
# 1234.56	      int或float
# true/false	  True/False
# null	       None

d = dict(name='Bob', age=20, score=88)
print(json.dumps(d))  # {"name": "Bob", "age": 20, "score": 88}

# dumps()方法返回一个str，内容就是标准的JSON。类似的，dump()方法可以直接把JSON写入一个file-like Object
# 要把JSON反序列化为Python对象，用loads()或者对应的load()方法，前者把JSON的字符串反序列化，后者从file-like Object中读取字符串并反序列化

json_str = '{"name": "Bob", "age": 20, "score": 88}'
print(json.loads(json_str))  # {'age': 20, 'score': 88, 'name': 'Bob'}


# Python的dict对象可以直接序列化为JSON的{}，但很多时候，我们更喜欢用class表示对象，比如定义Student类，然后序列化：

class Student(object):
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score


def student2dict(std):
    return {
        'name': std.name,
        'age': std.age,
        'score': std.score
    }


def dict2student(d):
    return Student(d['name'], d['age'], d['score'])


s = Student('Grace', 22, 99)
# print(json.dumps(s))  # 得到一个TypeError,错误的原因是Student对象不是一个可序列化为JSON的对象
print(json.dumps(d, default=student2dict))  # {"name": "Bob", "age": 20, "score": 88}

# 但是下次如果遇到一个其他类的实例，照样无法序列化为JSON。我们可以偷个懒，把任意class的实例变为dict
# 因为通常class的实例都有一个__dict__属性，它就是一个dict，用来存储实例变量。也有少数例外，比如定义了__slots__的class
print(json.dumps(d, default=lambda obj: obj.__dict__))  # {"name": "Bob", "age": 20, "score": 88}

# 如果我们要把JSON反序列化为一个Student对象实例，loads()方法首先转换出一个dict对象，然后，我们传入的object_hook函数负责把dict转换为Student实例：
json_str = '{"name": "Bob", "age": 20, "score": 88}'
print(json.loads(json_str, object_hook=dict2student))  # <__main__.Student object at 0x011F8550> 打印出的是反序列化的Student实例对象

# ensure_ascii
print(json.dumps('你好'))
# "\u4f60\u597d" 输出的是 ASCII字符码，这是因为json.dumps 序列化时对中文默认使用的ascii编码.想输出真正的中文需要指定ensure_ascii=False
print(json.dumps('你好', ensure_ascii=False)) # "你好"
