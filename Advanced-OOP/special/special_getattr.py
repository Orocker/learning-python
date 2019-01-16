# -*- coding: utf-8 -*-

# 正常情况下，当我们调用类的方法或属性时，如果不存在，就会报错。比如定义Student类：


class Student(object):
    def __init__(self):
        self.name = "michel"

    # 当调用不存在的属性时，比如score，Python解释器会试图调用__getattr__(self, 'score')
    # 来尝试获得属性,也可以返回函数
    def __getattr__(self, attr):
        if attr == 'score':
            return 66
        if attr == 'age':
            return lambda: 25
        # 此外，注意到任意调用如s.abc都会返回None，这是因为我们定义的__getattr__默认返回就是None。要让class只响应特定的几个属性，我们就要按照约定，抛出AttributeError的错误：
        # 这实际上可以把一个类的所有属性和方法调用全部动态化处理了，不需要任何特殊手段。
        # 这种完全动态调用的特性有什么实际作用呢？作用就是，可以针对完全动态的情况作调用。
        raise AttributeError('\'Student\' object has no attribute \'%s\'' % attr)


s = Student()
print("name:", s.name)
# 注意，只有在没有找到属性的情况下，才调用__getattr__，已有的属性，比如name，不会在__getattr__中查找。
print("score:", s.score)
print("age:", s.age())


# print(s.abc)


# 现在很多网站都搞REST API：
# http://api.server/user/friends
# http://api.server/user/timeline/list
# 如果要写SDK，给每个URL对应的API都写一个方法，那工作量会很大，而且，API一旦改动，SDK也要改。
# 利用完全动态的__getattr__，可以写出一个链式调用：

class Chain(object):
    def __init__(self, path=''):
        self._path = path

    def __getattr__(self, path):
        return Chain('%s/%s' % (self._path, path))

    def __str__(self):
        return self._path

    # 调用时，需要把:user替换为实际用户名。如果我们能写出这样的链式调用：
    def __call__(self, params):
        return Chain('%s/%s' % (self._path, params))

    __repr__ = __str__


print(Chain().status.user.timeline.list)  # /status/user/timeline/list

# 带参数的url
paramsChain = Chain('')
print(paramsChain.users('michel').page(20).repos)  # /users/michel/page/20/repos
