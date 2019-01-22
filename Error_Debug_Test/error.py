# -*- coding: utf-8 -*-


# 调用栈
# 如果错误没有被捕获，它就会一直往上抛，最后被Python解释器捕获，打印一个错误信息，然后程序退出。

def foo(s):
    return 10 / int(s)


def bar(s):
    return foo(s) * 2


def main():
    bar('0')


main()

# $ python error.py
# Traceback (most recent call last):      #错误的跟踪信息
#   File "error.py", line 19, in <module>
#     main()
#   File "error.py", line 16, in main  # 调用main()出错了，在代码文件error.py的第19行代码，但原因是第16行：
#     bar('0')
#   File "error.py", line 12, in bar  # 调用bar('0') 出错了，在代码文件error.py的第19行代码，但原因是第12行：
#     return foo(s) * 2  # 原因是return foo(s) * 2这个语句出错了，但这还不是最终原因
#   File "error.py", line 8, in foo  # 原因是return foo(s) * 2这个语句出错了，但这还不是最终原因
#     return 10 / int(s) # 原因是return 10 / int(s)这个语句出错了，这是错误产生的源头，因为下面打印了：
# ZeroDivisionError: division by zero # 根据错误类型ZeroDivisionError，由此判断，int(s)本身并没有出错，但是int(s)返回0，在计算10 / 0时出错，至此，找到错误源头。



