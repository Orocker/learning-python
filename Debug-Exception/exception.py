# -*- coding: utf-8 -*-

# 当我们某些代码可能会出错时，就可以用try来运行这段代码，如果执行出错，则后续代码不会继续执行，而是直接跳转至错误处理代码，即except语句块
# ，执行完except后，如果有finally语句块，则执行finally语句块，至此，执行完毕。
# 下面的代码在计算10 / 0 时会产生一个除法运算错误：
# try...
# except: division by zero
# finally...
# END

# 10 / 2
# try...
# result: 5.0
# finally...
# END


try:
    print('try...')
    r = 10 / 2
    print('result:', r)
except ZeroDivisionError as e:
    print('except:', e)
finally:
    print('finally...')
print('END')

# 错误应该有很多种类，如果发生了不同类型的错误，应该由不同的except语句块处理。没错，可以有多个except来捕获不同类型的错误：
# int()函数可能会抛出ValueError，所以用一个except捕获ValueError，用另一个except捕获ZeroDivisionError。
# 此外，如果没有错误发生，可以在except语句块后面加一个else，当没有错误发生时，会自动执行else语句：

try:
    print('try...')
    r = 10 / int('a')
    print('result', r)
except ValueError as e:
    print('ValueError', e)
except ZeroDivisionError as e:
    print('ZeroDivisionError', e)
else:
    print('No Error', r)
finally:
    print('finally...')
print('END')

# Python的错误其实也是class，所有的错误类型都继承自BaseException，所以在使用except时需要注意的是，它不但捕获该类型的错误，还把其子类也“一网打尽”。比如：
# 第二个except永远也捕获不到UnicodeError，因为UnicodeError是ValueError的子类，如果有，也被第一个except给捕获了。
# Python所有的错误都是从BaseException类派生的，常见的错误类型和继承关系 : https://docs.python.org/3/library/exceptions.html#exception-hierarchy
try:
    foo()
except ValueError as e:
    print('ValueError')
except UnicodeError as e:
    print('UnicodeError')


# 使用try...except捕获错误还有一个巨大的好处，就是可以跨越多层调用，比如函数main()调用foo()，foo()调用bar()，结果bar()出错了，这时，只要main()捕获到了，就可以处理：
# 也就是说，不需要在每个可能出错的地方去捕获错误，只要在合适的层次去捕获错误就可以了。这样一来，就大大减少了写try...except...finally的麻烦

def foo(s):
    return 10 / int(s)


def bar(s):
    return foo(s) * 2


def main():
    try:
        r = bar('a')
        print(r)
    except Exception as e:
        print('Error', e)
    finally:
        print('finally...')


main()
