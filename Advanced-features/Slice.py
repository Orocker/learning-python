# -*- coding: utf-8 -*-
def trim(s):
    if (s[:1] == ' '):
        return trim(s[1:])
    elif (s[-1:] == ' '):
        return trim(s[:-1])
    else:
        return s


print(trim(' test'))
print(trim(' test '))
