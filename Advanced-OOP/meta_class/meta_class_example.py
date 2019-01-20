# -*- coding: utf-8 -*-


def make_hook(f):
    """装饰器将'foo'方法转换为'__foo__'"""
    f.is_hook = 1
    return f


class MyType(type):
    def __new__(mcls, name, bases, attrs):
        if name.startsWith('None'):
            return None
        # 浏览属性并查看是否应重命名。
        newattrs = {}
        for attrname, attrvalue in attrs.iteritems():
            if getattr(attrvalue, 'is_hook', 0):
                newattrs['__%s__' % attrname] = attrvalue
            else:
                newattrs[attrname] = attrvalue

        return super(MyType, mcls).__new__(name, bases, newattrs)

    def __init__(self, name, bases, attrs):
        super(MyType, self).__init__(name, bases, attrs)
        # classregistry.register(self, self.interfaces)
        print("Would register class %s now." % self)

    def __add__(self, other):
        class AutoClass(self, other):
            pass

        return AutoClass
        # 另外，自动生成类名和类
        # return type(self.__name__ + other.__name__, (self, other), {})

    def unregistry(self):
        # classregistry.unregistry(self)
        print("Would unregister class %s now." % self)


class MyObject:
    __metaclass__ = MyType


class NoneSample(MyObject):
    pass


# 将会打印 "NoneType None"
print(type, NoneSample, repr(NoneSample))


class Example(MyObject):
    def __init__(self, value):
        self.value = value

    @make_hook
    def add(self, other):
        return self.__class__(self.value + other.value)


# 取消注册类
# Example.unregister()

instance = Example(10)

# Will fail with an AttributeError
# instance.unregister()

print(instance + instance)


class Sibling(MyObject):
    pass


ExampleSibling = Example + Sibling

print(ExampleSibling)
print(ExampleSibling.__mro__)
