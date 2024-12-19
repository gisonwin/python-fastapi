from sqlmodel import SQLModel, create_engine, Field

engine = create_engine('mysql+mysqldb://root:root@localhost:3306/hq?charset=utf8')


class UserBase(SQLModel):
    name: str
    nick_name: str | None = None
    password: str
    email: str | None = None


class User(UserBase, table=True):
    id: int | None = Field(default=None, primary_key=True)


SQLModel.metadata.create_all(engine)
