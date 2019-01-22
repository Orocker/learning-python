# -*- coding: utf-8 -*-

# 抛出错误
# 如果错误是class，捕获一个错误就是捕获到该class的一个实例。因此，错误并不是凭空产生的，而是有意创建并抛出的。Python的内置函数会抛出很多类型的错误，自己编写的函数也可以抛出错误。
# 如果要抛出错误，首先根据需要，可以定义一个错误的class，选择好继承关系，然后，用raise语句抛出一个错误的实例：
# 只有在必要的时候才定义我们自己的错误类型。如果可以选择Python已有的内置的错误类型（比如ValueError，TypeError），尽量使用Python内置的错误类型。


class FooError(ValueError):
    pass


def foo(s):
    n = int(s)
    if n == 0:
        raise FooError('Invalid Error: %s' % s)
    return 10 / s


foo('0')

# $ python throw_error.py
# Traceback (most recent call last):
#   File "throw_error.py", line 19, in <module>
#     foo('0')
#   File "throw_error.py", line 15, in foo
#     raise FooError('Invalid Error: %s' % s)
# __main__.FooError: Invalid Error: 0
