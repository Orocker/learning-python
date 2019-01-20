# -*- coding: utf-8 -*-


# 当Python解释器载入hello模块时，就会依次执行该模块的所有语句，执行结果就是动态创建出一个Hello的class对象，测试如下：
# >>> from hello import Hello
# >>> h = Hello()
# >>> h.hello()
# Hello , World
# >>> print(type(Hello))
# <class 'type'>
# >>> print(type(h))
# <class 'hello.Hello'>


# type()函数可以查看一个类型或变量的类型，Hello是一个class，它的类型就是type，而h是一个实例，它的类型就是class Hello。
# class的定义是运行时动态创建的，而创建class的方法就是使用type()函数。
# type()函数既可以返回一个对象的类型，又可以创建出新的类型，比如，可以通过type()函数创建出Hello类，而无需通过class Hello(object)...的定义：

def fn(self, name='World'):
    print("Hello , %s." % name)


Hello = type("Hello", (object,), dict(hello=fn))  # 创建Hello Class
h = Hello()
print(h.hello())
print("type of Hello:", type(Hello))
print("type of h:", type(h))


# 要创建一个class对象，type()函数依次传入3个参数：
#
# class的名称；
# 继承的父类集合，注意Python支持多重继承，如果只有一个父类，别忘了tuple的单元素写法；
# class的方法名称与函数绑定，这里我们把函数fn绑定到方法名hello上。


# metaclass

# metaclass，直译为元类，简单的解释就是：
# 当定义了类以后，就可以根据这个类创建出实例，所以：先定义类，然后创建实例。
# 但是如果想创建出类呢？那就必须根据metaclass创建出类，所以：先定义metaclass，然后创建类。
# 连接起来就是：先定义metaclass，就可以创建类，最后创建实例。
# 连所以，metaclass允许你创建类或者修改类。换句话说，你可以把类看成是metaclass创建出来的“实例”。


# metaclass是类的模板，所以必须从`type`类型派生：
class ListMetaclass(type):
    def __new__(cls, name, bases, attrs):
        attrs['add'] = lambda self, value: self.append(value)
        return type.__new__(cls, name, bases, attrs)


class MyList(list, metaclass=ListMetaclass):
    pass


# 当传入关键字参数metaclass时，魔术就生效了，它指示Python解释器在创建MyList时，要通过ListMetaclass.__new__()来创建，在此，我们可以修改类的定义，比如，加上新的方法，然后，返回修改后的定义。
#
# __new__()方法接收到的参数依次是：
#
# 1.当前准备创建的类的对象；
#
# 2.类的名字；
#
# 3.类继承的父类集合；
#
# 4.类的方法集合。

L = MyList()
L.add(100)
print("result for L add:", L)

