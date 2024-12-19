import asyncio


async def func():
    print(1)
    await asyncio.sleep(2)
    print(2)
    return 3


# async def test():
#     print("begin main")
#     # 创建Task对象，将当前执行func函数回到事件循环中
#     task1 = asyncio.create_task(func())
#     task2 = asyncio.create_task(func())
#
#     print("end main")
#
#     ret1 = await task1
#     ret2 = await task2
#     print(ret1, ret2)
#
#
# asyncio.run(test())


async def func_test():
    print("begin main")
    # 创建Task对象，将当前执行func函数回到事件循环中
    task_list = [
        asyncio.create_task(func(), name="t1"),
        asyncio.create_task(func(), name="t2")
    ]
    # task1 = asyncio.create_task(func())
    # task2 = asyncio.create_task(func())

    print("end main")

    # ret1 = await task1
    # ret2 = await task2
    done, pending = await asyncio.wait(task_list, timeout=None)
    print(done)


async def func_test_2():
    print("begin main")
    # 创建Task对象，将当前执行func函数回到事件循环中
    task_list = [
        asyncio.create_task(func(), name="t1"),
        asyncio.create_task(func(), name="t2")
    ]
    print("end main")

    done, pending = await asyncio.wait(task_list, timeout=None)
    print(done)


# asyncio.run(func_test())
asyncio.run(func_test_2())
