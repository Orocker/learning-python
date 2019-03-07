# -*- coding: utf-8 -*-
import time, random, queue
from multiprocessing.managers import BaseManager

# 发送任务队列
task_queue = queue.Queue()
# 接收任务队列
result_queue = queue.Queue()


class QueueManager(BaseManager):
    pass


# 把两个Queue都注册到网络上, callable参数关联了Queue对象:
QueueManager.register('get_task_queue', callable=lambda: task_queue)
QueueManager.register('get_result_queue', callable=lambda: result_queue)
# 绑定端口5000, 设置验证码'abc':
manager = QueueManager(address=('', 5000), authkey=b'abc')
# 启动queue
manager.start()
# 获得通过网络访问的Queue对象:
task = manager.get_task_queue()
result = manager.get_result_queue()
# 放任务到发送任务队列
for i in range(10):
    n = random.randint(0, 10000)
    print("Put task %d..." % n)
    task.put(n)

# 从result队列读取结果:
print("Try get results...")
for i in range(10):
    r = result.get(timeout=10)
    print("Results %s" % r)

manager.shutdown()
print("master exit.")

