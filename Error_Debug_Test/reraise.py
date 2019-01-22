# -*- coding: utf-8 -*-

# 在bar()函数中，我们明明已经捕获了错误，但是，打印一个ValueError!后，又把错误通过raise语句抛出去了，这不有病么？
# 其实这种错误处理方式不但没病，而且相当常见。捕获错误目的只是记录一下，便于后续追踪。但是，由于当前函数不知道应该怎么处理该错误，
# 所以，最恰当的方式是继续往上抛，让顶层调用者去处理。好比一个员工处理不了一个问题时，就把问题抛给他的老板，如果他的老板也处理不了，就一直往上抛，最终会抛给CEO去处理。
# raise语句如果不带参数，就会把当前错误原样抛出。


def foo(s):
    n = int(s)
    if n == 0:
        raise ValueError('Invalid Error: %s' % n)
    return 10 / n


def bar():
    try:
        foo('0')
    except ValueError as e:
        print('ValueError', e)
        raise


bar()


# $ python reraise.py
# ValueError Invalid Error: 0
# Traceback (most recent call last):
#   File "reraise.py", line 18, in <module>
#     bar()
#   File "reraise.py", line 13, in bar
#     foo('0')
#   File "reraise.py", line 7, in foo
#     raise ValueError('Invalid Error: %s' % n)
# ValueError: Invalid Error: 0

# 在except中raise一个Error，还可以把一种类型的错误转化成另一种类型：

def bar1():
    try:
        10 / 0
    except ZeroDivisionError:
        raise ValueError('Input Error')


bar1()

# 只要是合理的转换逻辑就可以，但是，决不应该把一个IOError转换成毫不相干的ValueError。
