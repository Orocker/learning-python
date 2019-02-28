# -*- coding: utf-8 -*-
import subprocess

# 很多时候，子进程并不是自身，而是一个外部进程。我们创建了子进程后，还需要控制子进程的输入和输出。
# print("$ nslookup www.python.org")
# r = subprocess.call(['nslookup', 'www.python.org'])
# print("Exit Code:", r)

# 如果子进程还需要输入，则可以通过communicate()方法输入：

print('$ nslookup')
p = subprocess.Popen(['nslookup'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
output, err = p.communicate(b'set q=mx\npython.org\nexit\n')
# print(output.decode("utf-8", 'ignore'))  # decode 默认使用strict模式
print(output.decode("gbk"))
print('Exit code:', p.returncode)

# $ nslookup
# ĬϷ:  UnKnown
# Address:  192.168.1.1
#
# > > :  UnKnown
# Address:  192.168.1.1
#
# python.org	MX preference = 50, mail exchanger = mail.python.org
# >
# Exit code: 0
#
# Process finished with exit code 0
