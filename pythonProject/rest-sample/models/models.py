from sqlmodel import Field, SQLModel, create_engine, Session, Relationship
from decimal import Decimal


# Team model
class TeamBase(SQLModel):
    name: str = Field(index=True)
    headquarters: str


class Team(TeamBase, table=True):
    id: int | None = Field(default=None, primary_key=True)
    heroes: list["Hero"] = Relationship(back_populates="team")


class TeamCreate(TeamBase):
    pass


class TeamPublic(TeamBase):
    id: int


class TeamUpdate(SQLModel):
    name: str | None = None
    headquarters: str | None = None


# Hero model
class HeroBase(SQLModel):
    name: str = Field(unique=True, index=True)
    secret_name: str
    age: int | None = Field(default=None, index=True)
    money: Decimal | None = Field(default=None, nullable=True, max_digits=8, decimal_places=3)

    team_id: int | None = Field(default=None, foreign_key="team.id")


class Hero(HeroBase, table=True):
    id: int | None = Field(default=None, primary_key=True)
    # hashed_password: str = Field(default=None)

    team: Team | None = Relationship(back_populates="heroes")

    # def __repr__(self):
    #     return f"Hero(id={self.id}, name={self.name}, secret_name={self.secret_name},age={self.age})"


class HeroCreate(HeroBase):
    # password: str
    pass


class HeroPublic(HeroBase):
    id: int


class HeroUpdate(SQLModel):
    name: str | None = None
    secret_name: str | None = None
    age: int | None = None
    # password: str | None = None
    team_id: int | None = None


class HeroPublicWithTeam(HeroPublic):
    team: TeamPublic | None = None


class TeamPublicWithHero(TeamPublic):
    heroes: list["Hero"] = []


# db config
db_name = "hq"
user = "root"
password = "root"
host = "localhost"
port = "3306"
url = f"mysql+pymysql://{user}:{password}@{host}:{port}/{db_name}?charset=utf8"

connect_args = {"check_same_thread": False}


def get_engine():
    engine = create_engine(url, echo=True)
    return engine


def get_session():
    with Session(get_engine()) as session:
        yield session
