import time
from concurrent.futures import Future
from concurrent.futures.thread import ThreadPoolExecutor
from concurrent.futures.process import ProcessPoolExecutor


def func(val):
    time.sleep(1)
    print(val)
    return val


t_pool = ThreadPoolExecutor(max_workers=5, thread_name_prefix='pool-')

# create process poll
# p_pool = ProcessPoolExecutor(max_workers=5)

for i in range(5):
    future = t_pool.submit(func, i)
    print(future)
