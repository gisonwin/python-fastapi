import sqlalchemy
from sqlalchemy import String, Integer, Date

engine = sqlalchemy.create_engine("mysql://root:root@192.168.236.188:3306/testdb", echo=True)
meta_data = sqlalchemy.MetaData()

person_table = sqlalchemy.Table(
    "person", meta_data,
    sqlalchemy.Column("id", Integer, primary_key=True),
    sqlalchemy.Column("name", String(128), nullable=False, unique=True),
    sqlalchemy.Column("age", Integer, nullable=False),
    sqlalchemy.Column("birthday", Date, nullable=False),
)

meta_data.create_all(engine)
