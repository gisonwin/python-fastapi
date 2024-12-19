import sqlalchemy
from sqlalchemy import String, Integer, Date

engine = sqlalchemy.create_engine("mysql://root:root@192.168.236.188:3306/testdb", echo=True)
meta_data = sqlalchemy.MetaData()

person = sqlalchemy.Table(
    "person", meta_data,
    sqlalchemy.Column("id", Integer, primary_key=True),
    sqlalchemy.Column("name", String(128), nullable=False, unique=True),
    sqlalchemy.Column("age", Integer, nullable=False),
    sqlalchemy.Column("birthday", Date, nullable=False),
)

meta_data.create_all(engine)

# insert a person
# person_insert = person.insert()
# print(person_insert)
# insert_tom = person_insert.values(name="White", age=20, birthday="2022-02-22")
# with engine.connect() as connection:
#     rs = connection.execute(insert_tom)
#     print(rs.inserted_primary_key)
#     connection.commit()


# batch insert persons
person_insert = person.insert()
with engine.connect() as connection:
    rs = connection.execute(person_insert, [
        {"name": "John5", "age": 20, "birthday": "1990-01-19"},
        {"name": "John6", "age": 30, "birthday": "1990-02-19"},
        {"name": "John7", "age": 40, "birthday": "1990-03-19"},
        {"name": "John8", "age": 50, "birthday": "1990-04-19"},
    ])
    connection.commit()
    print(rs.inserted_primary_key_rows)
