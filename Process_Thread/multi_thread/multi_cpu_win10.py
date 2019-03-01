from multiprocessing import Pool
import threading
import multiprocessing


def loop(i):
    x = 0
    print("Thread %d" % i)
    while True:
        x = x ^ 1


def run_process(j, cpu_counts):
    print("Process : %d" % i)
    for j in range(cpu_counts * 2):
        t = threading.Thread(target=loop, args=(j,))
        t.start()


if __name__ == '__main__':
    cpu_count = multiprocessing.cpu_count()
    p = Pool(cpu_count)
    for i in range(cpu_count):
        p.apply_async(run_process, args=(i,cpu_count))
    p.close()
    p.join()