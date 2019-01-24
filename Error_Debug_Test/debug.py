# -*- coding: utf-8 -*-
import logging
import pdb

logging.basicConfig(level=logging.INFO)


# 1：print()调试Bug
# $ python debug.py
# >>> n = 0
# Traceback (most recent call last):
#   File "debug.py", line 16, in <module>
#     main()
#   File "debug.py", line 13, in main
#     foo('0')
#   File "debug.py", line 9, in foo
#     return 10 / n
# ZeroDivisionError: division by zero


def print_error(s):
    n = int(s)
    print(">>> n = %d" % n)
    return 10 / n


# print_error('0')


# main()


# 用print()最大的坏处是将来还得删掉它
# 2：断言 凡是用print()来辅助查看的地方，都可以用断言（assert）来替代：

# assert的意思是，表达式n != 0应该是True，否则，根据程序运行的逻辑，后面的代码肯定会出错。
# 如果断言失败，assert语句本身就会抛出AssertionError：

# $ python debug.py
# Traceback (most recent call last):
#   File "debug.py", line 43, in <module>
#     main1()
#   File "debug.py", line 40, in main1
#     bar('0')
#   File "debug.py", line 35, in bar
#     assert n != 0, 'n is zero'
# AssertionError: n is zero


def assert_error(s):
    n = int(s)
    assert n != 0, 'n is zero'
    return 10 / n


# assert_error('0')


# 程序中如果到处充斥着assert，和print()相比也好不到哪去。不过，启动Python解释器时可以用-O参数来关闭assert：
# 关闭后，你可以把所有的assert语句当成pass来看。
# python -O debug.py


# 3: logging : 和assert比，logging不会抛出错误，而且可以输出到文件：
# logging.info()就可以输出一段文本。 # 设置 logging.basicConfig(level=logging.INFO)
# 这就是logging的好处，它允许你指定记录信息的级别，有debug，info，warning，error等几个级别，当指定level=INFO时，
# logging.debug就不起作用了。同理，指定level=WARNING后，debug和info就不起作用了。这样一来，你可以放心地输出不同级别的信息，也不用删除，最后统一控制输出哪个级别的信息。
# logging的另一个好处是通过简单的配置，一条语句可以同时输出到不同的地方，比如console和文件。

# $ python debug.py
# INFO:root:n = 0
# Traceback (most recent call last):
#   File "debug.py", line 72, in <module>
#     d = logging_error('0')
#   File "debug.py", line 69, in logging_error
#     return 10 / n
# ZeroDivisionError: division by zero


def logging_error(s):
    n = int(s)
    logging.info("n = %d" % n)
    return 10 / n


# d = logging_error('0')
# print(d)


# 4: PDB 它是启动Python的调试器pdb，让程序以单步方式运行，可以随时查看运行状态： 见pdb_debug.py

# $ python -m pdb debug.py
# > e:\py\learning-python\error_debug_test\debug.py(2)<module>()
# -> import logging


# 5:pdb.set_trace()  这个方法也是用pdb，但是不需要单步执行，只需要import pdb，然后，在可能出错的地方放一个pdb.set_trace()，就可以设置一个断点：
# 运行代码，程序会自动在pdb.set_trace()暂停并进入pdb调试环境，可以用命令p查看变量，或者用命令c继续运行
# $ python debug.py
# > e:\py\learning-python\error_debug_test\debug.py(103)pdb_error()
# -> print(10 / n)
# (Pdb) p n
# 0
# (Pdb) p s
# '0'
# (Pdb) c
# Traceback (most recent call last):
#   File "debug.py", line 106, in <module>
#     pdb_error('0')
#   File "debug.py", line 103, in pdb_error
#     print(10 / n)
# ZeroDivisionError: division by zero


def pdb_error(s):
    n = int(s)
    pdb.set_trace()
    print(10 / n)


pdb_error('0')
