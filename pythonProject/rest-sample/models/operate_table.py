from models import Hero, get_engine
from sqlmodel import select, or_, col, Session

engine = get_engine()


def query_hero(hero_name: str):
    with Session(engine) as session:
        statement = select(Hero).where(Hero.name == hero_name)
        h = session.execute(statement).first()
        print(h)


def query_heroes(h: Hero | None = None):
    """
     query all heroes in database
    :return: heroes list
    """
    with engine.connect() as conn:
        if h is None:
            return conn.execute(select(Hero)).all()
        elif h.name is not None and h.age is not None:
            # return conn.execute(select(Hero).where(Hero.name == h.name).where(Hero.age > h.age)).all()
            # return conn.execute(select(Hero).where((col(Hero.name) == h.name, col(Hero.age) > h.age))).all()
            # return conn.execute(select(Hero).where(or_(col(Hero.name) == h.name, col(Hero.age) > h.age))).all()
            return conn.execute(
                select(Hero).where(or_(col(Hero.name) == h.name, col(Hero.age) > h.age)).offset(0).limit(3)
            ).all()
        elif h.age is not None:
            return conn.execute(select(Hero).where(Hero.age > h.age)).all()
        # else:
        #     return conn.execute(select(Hero)).all()


def query_one_hero(h: Hero | None = None):
    with engine.connect() as conn:
        if h is None:
            return conn.execute(select(Hero)).first()
        else:
            # return conn.execute(select(Hero).where(Hero.name == h.name)).first()
            # only one record can use one() method return result
            return conn.execute(select(Hero).where(Hero.name == h.name)).one()


def get_one_hero_by_id(hero_id):
    with Session(engine) as conn:
        return conn.get(Hero, hero_id)


# query_hero('Spider-Boy')
heroes = query_heroes(Hero(name="Rust-Man", age=35))
for hero in heroes:
    print(hero)
print("*" * 20)
one_hero = query_one_hero(Hero(name="Rust-Man"))
print(one_hero)

one_hero = get_one_hero_by_id(1)
print(one_hero)
