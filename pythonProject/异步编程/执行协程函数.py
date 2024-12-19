#!-*- coding:utf-8 -*-
import asyncio


async def func():
    print("invoke func")


result = func()
# loop = asyncio.get_event_loop()
# loop.run_until_complete(func())
asyncio.run(result)  # python 3.7+
