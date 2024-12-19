import uvicorn
from fastapi import FastAPI, HTTPException, Query, Depends
from sqlmodel import Session, select
from models.models import HeroCreate, TeamCreate, HeroPublic, TeamPublic, Hero, Team, HeroUpdate, TeamUpdate, \
    get_session, HeroPublicWithTeam, TeamPublicWithHero

app = FastAPI()


# @asynccontextmanager
# async def lifespan():
#     create_db_and_tables()
#     yield
#     SQLModel.metadata.clear()

def hash_password(password: str) -> str:
    return f"hashed password {password} here"


@app.post("/heroes/", response_model=HeroPublic)
async def create_hero(*, session: Session = Depends(get_session), hero: HeroCreate):
    hashed_password = hash_password(hero.password)
    # with Session(engine) as session:
    extra_data = {"hashed_password": hashed_password}
    add_hero = Hero.model_validate(hero, update=extra_data)
    session.add(add_hero)
    session.commit()
    session.refresh(add_hero)
    return add_hero


@app.get("/heroes/", response_model=list[HeroPublic])
async def read_heroes(*, session: Session = Depends(get_session), offset: int = 0,
                      limit: int = Query(default=100, le=100)):
    # with Session(engine) as session:
    statement = select(Hero).offset(offset).limit(limit)
    return session.exec(statement).all()


@app.get("/heroes/{hero_id}", response_model=HeroPublicWithTeam)
async def read_hero(*, session: Session = Depends(get_session), hero_id: int):
    # with Session(engine) as session:
    hero = session.get(Hero, hero_id)
    if not hero:
        raise HTTPException(status_code=404, detail=f"Hero id={hero_id} not found")
    return hero


@app.patch("/heroes/{hero_id}", response_model=HeroPublic)
async def update_hero(*, session: Session = Depends(get_session), hero_id: int, hero_update: HeroUpdate):
    # with Session(engine) as session:
    db_hero = session.get(Hero, hero_id)
    if not db_hero:
        raise HTTPException(status_code=404, detail=f"Hero={hero_id} not found")
    hero_data = hero_update.model_dump(exclude_unset=True)
    extra_data = {}
    if "password" in hero_data:
        password = hero_data["password"]
        hashed_password = hash_password(password)
        extra_data["password"] = hashed_password
    db_hero.sqlmodel_update(hero_data, update=extra_data)
    session.add(db_hero)
    session.commit()
    session.refresh(db_hero)
    return db_hero


@app.delete("/heroes/{hero_id}")
async def delete_hero(*, session: Session = Depends(get_session), hero_id: int):
    # with Session(engine) as session:
    del_hero = session.get(Hero, hero_id)
    if not del_hero:
        raise HTTPException(status_code=404, detail=f"Hero={hero_id} not found")
    session.delete(del_hero)
    session.commit()
    return {"ok": True}


# team
@app.post("/teams/", response_model=TeamPublic)
async def create_team(*, session: Session = Depends(get_session), team: TeamCreate):
    add_team = Team.model_validate(team)
    session.add(add_team)
    session.commit()
    session.refresh(add_team)
    return add_team


@app.get("/teams/", response_model=list[TeamPublic])
async def read_teams(*, session: Session = Depends(get_session), offset: int = 0,
                     limit: int = Query(default=100, le=100)):
    statement = select(Team).offset(offset).limit(limit)
    return session.exec(statement).all


@app.get("/teams/{team_id}", response_model=TeamPublicWithHero)
async def read_team(*, session: Session = Depends(get_session), team_id: int):
    query_team = session.get(Team, team_id)
    if not query_team:
        raise HTTPException(status_code=404, detail=f"Team id={team_id} not found")
    return query_team


@app.patch("/teams/{team_id}", response_model=TeamPublic)
async def update_team(*, session: Session = Depends(get_session), team_id: int, team: TeamUpdate):
    db_team = session.get(Team, team_id)
    if not db_team:
        raise HTTPException(status_code=404, detail=f"Team id={team_id} not found")
    team_data = team.model_dump(exclude_unset=True)
    for k, v in team_data.items():
        setattr(db_team, k, v)
    session.add(db_team)
    session.commit()
    session.refresh(db_team)
    return db_team


@app.delete("/teams/{team_id}")
async def delete_team(*, session: Session = Depends(get_session), team_id: int):
    del_team = session.get(Team, team_id)
    if not del_team:
        raise HTTPException(status_code=404, detail=f"Team id={team_id} not found")
    session.delete(del_team)
    session.commit()
    return {"ok": True}


if __name__ == '__main__':
    uvicorn.run(app='main:app', host='0.0.0.0', port=8800, reload=True)
