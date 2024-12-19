from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

from models import DataBlock

engine = create_engine('taosrest://root:taosdata@124.70.89.186:6041/ht2_data', echo=True)
db_session = sessionmaker(bind=engine)
session = db_session()
rs = session.query(DataBlock).count()
print(rs)
session.close()
