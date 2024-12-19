# def func():
#     print('当前是一个生成器函数')
#     while True:
#         yield '生成器函数返回数据'
#
#
# obj = func()
# # print(obj)
# print(next(obj))
# print(next(obj))

# 利用生成器特点进行任务切换
import time


def func_a():
    while True:
        print('func_a()')
        yield
        time.sleep(0.5)


def func_b(obj):
    while True:
        print('func_b(obj)')
        obj.__next__()


a = func_a()
func_b(a)
