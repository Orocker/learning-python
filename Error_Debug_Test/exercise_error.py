# -*- coding: utf-8 -*-

from functools import reduce


# debug 下面代码
# 1 int() -> float()
# def str2nums(s):
#     return int(s)

# 2 try... except...
# def str2nums(s):
#     try:
#         return int(s)
#     except ValueError as e:
#         return float(s)


def str2nums(s):
    return int(s)


def calc(exp):
    ss = exp.split('+')
    ns = map(str2nums, ss)
    return reduce(lambda acc, x: acc + x, ns)


def main():
    r = calc('100+200+345')
    print('100+200+345 = ', r)
    r = calc('99 + 88 + 7.6')
    print('99 + 88 + 7.6 =', r)


main()

# 总结
# Python内置的try...except...finally用来处理错误十分方便。出错时，会分析错误信息并定位错误发生的代码位置才是最关键的。
# 程序也可以主动抛出错误，让调用者来处理相应的错误。但是，应该在文档中写清楚可能会抛出哪些错误，以及错误产生的原因。
