# -*- coding: utf-8 -*-
from datetime import datetime
# 获取当前日期和时间
now = datetime.now()
print(now) # 2019-03-26 14:25:42.798240
print(type(now)) # <class 'datetime.datetime'>

# datetime是模块，datetime模块还包含一个datetime类，通过from datetime import datetime导入的才是datetime这个类

# 获取指定日期和时间
dt = datetime(2019, 3, 26, 14, 50, 00)
print(dt)

# datetime to timestamp
print(dt.timestamp())  # 1553583000.0 Python的time# stamp是一个浮点数。如果有小数位，小数位表示毫秒数。

# timestamp to datetime
t = 1553593758.0
dt1 = datetime.fromtimestamp(t)
print(dt1) # 2019-03-26 17:49:18

# 到timestamp是一个浮点数，它没有时区的概念，而datetime是有时区的。上述转换是在timestamp和本地时间做转换。

# timestamp 转换 UTC 标准时区

t1 = 1553593758.0
dt2 = datetime.fromtimestamp(t1)  # 本地时间
utc_dt = datetime.utcfromtimestamp(t1)  # UTC标准时间

# str to datetime

today = datetime.strptime('2019-03-26 17:57:00', '%Y-%m-%d %H:%M:%S')
print(today) # 2019-03-26 17:57:00

# datetime to str
print(now.strftime('%a, %b %d %H:%M')) # Tue, Mar 26 18:00
print(now.strftime('%Y-%m-%d %H:%M:%S')) # T2019-03-26 18:00:35

