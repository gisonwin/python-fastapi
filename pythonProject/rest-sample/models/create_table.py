from sqlmodel import SQLModel, Session
from models import Hero, get_engine, Team


def create_tables():
    engine = get_engine()
    SQLModel.metadata.create_all(engine)

    hero_1 = Hero(name="Dead pond", secret_name="Dive Wilson", age=18, money=12.5)
    hero_2 = Hero(name='Spider-Boy', secret_name='Pedro Parquetry', age=30, money=12348.567)
    hero_3 = Hero(name="Rust-Man", secret_name="Tommy Sharp", age=48, money=1.101)
    hero_4 = Hero(name="Tarantula", secret_name="Natalia Roman-on", age=32, money=39.999)
    hero_5 = Hero(name="Black Lion", secret_name="Trevor Challa", age=35)
    hero_6 = Hero(name="Dr. Weird", secret_name="Steve Weird", age=36)
    hero_7 = Hero(name="Captain North America", secret_name="Esteban Rogelios", age=93)

    team1 = Team(name="Prevents", headquarters="Sharp Tower")
    team2 = Team(name="SHIELD", headquarters="SHIELD Group")
    team3 = Team(name="Z-Force", headquarters="Sister Margaret 's Bar")

    with Session(engine) as session:
        session.add(hero_1)
        session.add(hero_2)
        session.add(hero_3)
        session.add(hero_4)
        session.add(hero_5)
        session.add(hero_6)
        session.add(hero_7)
        session.add(team1)
        session.add(team2)
        session.add(team3)
        session.commit()


create_tables()
