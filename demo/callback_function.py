# -*- coding: utf-8 -*-
from event import *


def get_odd_number(k, get_even_number):
    return 1 + get_even_number(k)


def main():
    k = 1
    # 生成 2K + 1 的奇数
    i = get_odd_number(k, double)
    print(i)

    # 生成 4K + 1 的奇数

    i = get_odd_number(k, quadruple)
    print(i)

    # 生成 8K + 1 的奇数

    i = get_odd_number(k, lambda x: x * 8)
    print(i)


if __name__ == "__main__":
    main()