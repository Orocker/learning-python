# -*- coding: utf-8 -*-

# 当我们某些代码可能会出错时，就可以用try来运行这段代码，如果执行出错，则后续代码不会继续执行，而是直接跳转至错误处理代码，即except语句块
# ，执行完except后，如果有finally语句块，则执行finally语句块，至此，执行完毕。
# 下面的代码在计算10 / 0时会产生一个除法运算错误：
# try...
# except: division by zero
# finally...
# END

try:
    print('try...')
    r = 10 / 0
    print('result:', r)
except ZeroDivisionError as e:
    print('except:', e)
finally:
    print('finally...')
print('END')

