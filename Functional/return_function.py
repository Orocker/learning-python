# -*- coding: utf-8 -*-

# 返回函数

# 定义求和函数，不返回求和结果，根据需要在计算,调用lazy_sum()时，返回的不是求和结果，而是求和函数
def lazy_sum(*args):
    def sum():
        ax = 0
        for n in args:
            ax = ax + n
        return ax

    return sum


# f = lazy_sum(1, 3, 5, 7, 9)
# f
# <function lazy_sum.<locals>.sum at 0x01E385D0>
# f()
# 25

# 我们在函数lazy_sum中又定义了函数sum，并且，内部函数sum可以引用外部函数lazy_sum的参数和局部变量，
# 当lazy_sum返回函数sum时，相关参数和变量都保存在返回的函数中，这种称为“闭包（Closure）”的程序结构拥有极大的威力。

# 调用lazy_sum()时，每次调用都会返回一个新的函数，即使传入相同的参数： sum1()和sum2()的调用结果互不影响
sum1 = lazy_sum(1, 3, 5, 7, 9)
sum2 = lazy_sum(1, 3, 5, 7, 9)
sum1 == sum2  # False


# 闭包Closure

def count():
    fs = []
    for i in range(1, 4):
        def f():
            return i * i

        fs.append(f)
    return fs


count1, count2, count3 = count()


# 你可能认为调用f1()，f2()和f3()结果应该是1，4，9，但实际结果是：
# >>> count1()
# 9
# >>> count2()
# 9
# >>> count3()
# 9
# >>>
# 全部都是9！原因就在于返回的函数引用了变量i，但它并非立刻执行。等到3个函数都返回时，它们所引用的变量i已经变成了3，因此最终结果为9

# 如果一定要引用循环变量怎么办？方法是再创建一个函数，用该函数的参数绑定循环变量当前的值，无论该循环变量后续如何更改，已绑定到函数参数的值不变：

def counts():
    def f(j):
        def g():
            return j * j

        return g

    fs = []
    for i in range(1, 4):
        fs.append(f(i))
    return fs


countA, countB, countC = counts()
# >>> countA()
# 1
# >>> countB()
# 4
# >>> countC()
# 9
