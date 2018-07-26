# -*- coding: utf-8 -*-

dict = {'a':1,'b':2,'c':3}

#迭代key
for key in dict:
	print(key)

#迭代value
for value in dict.values():
	print(value)

#迭代key & value
for key1,value1 in dict.items():
	print('key:',key1,'value:',value1)