### 实现了__aiter__()和————anext__()方法的对象，__anext__必须返回一个awaitable对象，async_for会处理异步迭代器的__anext__方法所返回的可等待对象，
### 直到引发一个stopAsyncIteration异常，由PEP492引入。
### 可在asynic_for语句中被使用的对象，必须通过它的__aiter__()方法返回一个asynchronous iterator。

import asyncio


class AsyncContextManager:
    """
    通过定义__aenter__,__aexit__方法来对async_with语句中的环境进行控制
    """

    def __init__(self):
        self.conn = None

    async def do_sth(self):
        # 异步操作db
        return 666

    async def __aenter__(self):
        # 异步 连接db
        self.conn = await asyncio.sleep(1)
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        # 异步关闭db连接
        await asyncio.sleep(1)


async def async_context():
    async with AsyncContextManager() as af:
        result = await af.do_sth()
        print(result)


class Reader(object):
    """
    自定义异步迭代器，同时也是异步可迭代对象
    """

    def __init__(self):
        self.count = 0

    async def readline(self):
        self.count += 1
        if self.count == 100:
            return None
        return self.count

    def __aiter__(self):
        return self

    async def __anext__(self):
        val = await self.readline()
        if val is None:
            raise StopAsyncIteration
        return val


async def func():
    obj = Reader()
    async for val in obj:
        print(val)


if __name__ == '__main__':
    asyncio.run(func())
    asyncio.run(async_context())
