#!-*- coding:utf-8 -*-
import asyncio


async def func():
    print("invoke")
    response = await asyncio.sleep(2)
    print("finish", response)


asyncio.run(func())
