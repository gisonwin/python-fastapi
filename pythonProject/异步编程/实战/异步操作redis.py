### python操作redis时 都是网络IO，所以利用IO等待时提高效率。
### pip install aioredis,支持异步的redis
import asyncio
import aioredis


def get_redis(address, password, max_connections=10, decode_responses=True):
    # return aioredis.from_url('redis://124.70.89.186:26502', password="redis@sailmi", decode_responses=True,
    #                          max_connections=10)
    return aioredis.from_url(address, password=password, decode_responses=decode_responses,
                             max_connections=max_connections)


async def redis_hset():
    redis = get_redis('redis://124.70.89.186:26502', decode_responses=True, password="redis@sailmi")
    num = await redis.hset("hash", mapping={"name": "value1", "nick": "value2", "age": 123})
    print(num)
    result = await redis.hgetall("hash")
    print(result)
    assert result == {
        "name": "value1",
        "nick": "value2",
        "age": "123",  # note that Redis returns int as string
    }
    await redis.close()


async def execute_get_set():
    redis = aioredis.from_url('redis://124.70.89.186:26502', password="redis@sailmi")
    await redis.set("key", "string-value")
    value = await redis.get("key")
    print(value)
    assert value == b'string-value'
    redis = get_redis('redis://124.70.89.186:26502', decode_responses=True, password="redis@sailmi")
    str_value = await redis.get("key")
    assert str_value == "string-value"
    await redis.close()


async def redis_tran():
    redis = get_redis('redis://124.70.89.186:26502', decode_responses=True, password="redis@sailmi")
    async with redis.pipeline(transaction=True) as pipe:
        ok1, ok2 = await (pipe.set("key1", "value1").set("key2", "value2").execute())
        assert ok1
        assert ok2
        vl = pipe.mget("key1", "key2")
        print(type(vl))


if __name__ == '__main__':
    # 执行get set
    asyncio.run(execute_get_set())
    # 执行redis hset
    asyncio.run(redis_hset())
    # 执行transaction
    asyncio.run(redis_tran())
