import asyncio


async def hello_world():
    print('hello ')
    await asyncio.sleep(1)
    print('world')


asyncio.run(hello_world())
