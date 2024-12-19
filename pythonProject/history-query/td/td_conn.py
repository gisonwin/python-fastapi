from taosrest import connect, TaosRestConnection, TaosRestCursor


def check_database(con):
    cur = con.cursor()
    cur.execute('DROP DATABASE IF EXISTS power')
    cur.execute('CREATE DATABASE power')
    return cur


def insert_db(cur):
    cur.execute(
        "CREATE STABLE power.meters (ts TIMESTAMP, current FLOAT, voltage INT, phase FLOAT) TAGS (location BINARY(64), groupId INT)")

    # insert data
    cur.execute("""INSERT INTO power.d1001 USING power.meters TAGS('California.SanFrancisco', 2) VALUES ('2018-10-03 14:38:05.000', 10.30000, 219, 0.31000) ('2018-10-03 14:38:15.000', 12.60000, 218, 0.33000) ('2018-10-03 14:38:16.800', 12.30000, 221, 0.31000)
        power.d1002 USING power.meters TAGS('California.SanFrancisco', 3) VALUES ('2018-10-03 14:38:16.650', 10.30000, 218, 0.25000)
        power.d1003 USING power.meters TAGS('California.LosAngeles', 2) VALUES ('2018-10-03 14:38:05.500', 11.80000, 221, 0.28000) ('2018-10-03 14:38:16.600', 13.40000, 223, 0.29000)
        power.d1004 USING power.meters TAGS('California.LosAngeles', 3) VALUES ('2018-10-03 14:38:05.000', 10.80000, 223, 0.29000) ('2018-10-03 14:38:06.500', 11.50000, 221, 0.35000)""")
    print("inserted row count:", cur.rowcount)


def query_db(cur, sql):
    data = cur.execute(sql)
    return cur.rowcount

    # url="http://124.70.89.186:6041",


conn = connect(
    url="http://192.168.236.188:6041",
    user="root",
    password="taosdata",
    # database="power"
)
print(conn)
cursor = check_database(conn)
insert_db(cursor)
list_data = query_db(cursor, "SELECT * FROM power.meters limit 10")
print(list_data)
for row in cursor.fetchall():
    print(row)
cursor.close()
conn.close()
