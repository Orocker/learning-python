# -*- coding: utf-8 -*-
def trim(s):
    if (s[:1] == ' '):
        return trim(s[1:])
    elif (s[-1:] == ' '):
        return trim(s[:-1])
    else:
        return s

# print(trim(' dada'))
# print(trim(' dada1 '))

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