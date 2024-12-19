import sqlalchemy

engine = sqlalchemy.create_engine('mysql://root:root@192.168.236.188:3306/fastapi')
conn = engine.connect()
print(conn)

query = sqlalchemy.text("select * from fastapi.student")
rs = conn.execute(query)
print(rs)

for r in rs:
    print(r)

conn.close()

engine.dispose()
