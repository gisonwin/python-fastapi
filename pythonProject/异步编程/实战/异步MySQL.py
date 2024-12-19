## pip install aiomysql
import asyncio, aiomysql


async def execute(host, password, db):
    conn = await aiomysql.connect(host=host, port=3306, user='root', password=password, db=db)
    cur = await conn.cursor()
    await cur.execute("select * from teacher")
    result = await cur.fetchall()
    print(result)
    await cur.close()
    conn.close()


task_list = [
    # execute(host="127.0.0.1", password="root", db='fastapi'),
    execute(host="127.0.0.1", password="root", db='fastapi')
]

asyncio.run(asyncio.wait(task_list))
