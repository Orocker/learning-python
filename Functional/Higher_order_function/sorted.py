# -*- coding: utf-8 -*-
import math

#默认排序，从小到大排序
sorted([36, 5, -12, 9, -21]) #[-21, -12, 5, 9, 36]

#自定义排序
sorted([36, 5, -12, 9, -21]，key=abs)#[5, 9, -12, -21, 36]

#字符串排序，按ASCII码大小排序
sorted(['bob', 'about', 'Zoo', 'Credit'])#['Credit', 'Zoo', 'about', 'bob']

#反向从小到大排序
sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower, reverse=True)





