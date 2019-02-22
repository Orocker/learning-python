# -*- coding: utf-8 -*-
import os

# Unix/Linux环境下运行
print("Process (%s) start..." % os.getpid())

pid = os.fork()

if pid == 0:
    print("I am child process (%s) and my parent process is (%s)" % (os.getpid(), os.getppid()))
else:
    print("I (%s) just created a child process (%s).." % (os.getppid(), pid))

# Process (31332) start...
# I (31268) just created a child process (31333)..
# I am child process (31333) and my parent process is (31332)


