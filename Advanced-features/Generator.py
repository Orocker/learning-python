# -*- coding: utf-8 -*-

# 生成器 Generator

# 创建
gener = (x for x in range(10))

# 获取Generator下一个返回值，获取完后，抛出StopIteration错误
next(gener)

# 迭代Generator

for n in gener:
    print(n)


# for循环无法实现的时候，定义函数实现，如斐波那契数列


def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b  # 如果一个函数定义中包含yield关键字，这个函数就不再是一个普通函数，而是一个generator
        a, b = b, a + b
        n = n + 1
    return 'done'


# Generator 的执行过程,遇到yield就会中断，下次继续执行，直到没有yield，再执行就会报错

def odd():
    print('step1')
    yield 1
    print('step2')
    yield 3
    print('step3')
    yield 5


# Generator获取返回值，返回值必须捕获StopIteration错误，返回值包含在StopIteration的value中

data = fib(10)

while True:
    try:
        s = next(data)
        print('data:', s)
    except StopIteration as e:
        print('Generator return value:', e.value)
        break
