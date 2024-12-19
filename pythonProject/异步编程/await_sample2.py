import asyncio


async def func():
    print("invoke")
    response = await others()
    # await等待others函数 返回后 才进行下一个
    print("end..............", response)
    response1 = await others()
    print("end111..............", response1)


async def others():
    print("start")
    await asyncio.sleep(2)
    print("end")
    return '返回值'


asyncio.run(func())
