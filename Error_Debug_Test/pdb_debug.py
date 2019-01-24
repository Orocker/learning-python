# -*- coding: utf-8 -*-
s = '0'
n = int(s)
print(10 / n)

# $ python -m pdb pdb_debug.py
# > e:\py\learning-python\error_debug_test\pdb_debug.py(2)<module>()
# -> s = '0'
# (Pdb) l :查看代码
#   1     # -*- coding: utf-8 -*-
#   2  -> s = '0'
#   3     n = int(s)
#   4     print(10 / n)
# [EOF]
# (Pdb) n :单步执行代码
# > e:\py\learning-python\error_debug_test\pdb_debug.py(3)<module>()
# -> n = int(s)
# (Pdb) n
# > e:\py\learning-python\error_debug_test\pdb_debug.py(4)<module>()
# -> print(10 / n)
# (Pdb) p s ： p + 变量名 查看变量
# '0'
# (Pdb) p n
# 0
# (Pdb) q ：退出调试

# 这种通过pdb在命令行调试的方法理论上是万能的，但实在是太麻烦了
