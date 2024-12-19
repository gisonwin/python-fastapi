import asyncio
import requests


async def download_image(url):
    loop = asyncio.get_event_loop()
    # requests 只能同步模块 不支持asyncio,此处调用loop.run_in_executor
    future = loop.run_in_executor(None, requests.get, url)
    response = await future

    file_name = url.split('/')[-1]
    with open(file_name, 'wb') as f:
        f.write(response.content)


if __name__ == '__main__':
    url_lists = [
        'https://youimg1.c-ctrip.com/target/100a0g0000007n7d636CA.jpg',
        'https://youimg1.c-ctrip.com/target/100r10000000pycel4E0E.jpg',
        'https://n.sinaimg.cn/sinacn/w2048h1280/20180312/6706-fyscsmu5355528.jpg'
    ]
    tasks = [download_image(url) for url in url_lists]
    loop = asyncio.get_event_loop()
    # loop.run_until_complete(asyncio.gather(*tasks))
    loop.run_until_complete(asyncio.wait(tasks))
