import os

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env

SQLALCHEMY_DATABASE_URL = os.getenv("POSTGRESQL_URL")


# SQLALCHMY_DATABASE_URL = "postgresql://user:password@postgresserver/db"
# SQLALCHEMY_DATABASE_URL = os.getenv(POSTGRESQL_URL)

engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
conn = engine.connect()
print(conn.get_isolation_level())





# from typing import Annotated, Optional
#
# from fastapi import Depends, FastAPI, HTTPException, Query
# from sqlmodel import Field, Session, SQLModel, create_engine, select
#
#
# class HeroBase(SQLModel):
#     name: str = Field(index=True)
#     age: Optional[int] = Field(default=None, index=True)
#
#
# class Hero(HeroBase, table=True):
#     id: Optional[int] = Field(default=None, primary_key=True)
#     secret_name: str
#
#
# class HeroPublic(HeroBase):
#     id: int
#
#
# class HeroCreate(HeroBase):
#     secret_name: str
#
#
# class HeroUpdate(HeroBase):
#     name: Optional[str] = None
#     age: Optional[int] = None
#     secret_name: Optional[str] = None
#
#
# sqlite_file_name = "database.db"
# sqlite_url = f"sqlite:///{sqlite_file_name}"
#
# connect_args = {"check_same_thread": False}
# engine = create_engine(sqlite_url, connect_args=connect_args)
#
#
# def create_db_and_tables():
#     SQLModel.metadata.create_all(engine)
#
#
# def get_session():
#     with Session(engine) as session:
#         yield session
#
#
# SessionDep = Annotated[Session, Depends(get_session)]
# app = FastAPI()
#
#
# @app.on_event("startup")
# def on_startup():
#     create_db_and_tables()
#
#
# @app.post("/heroes/", response_model=HeroPublic)
# def create_hero(hero: HeroCreate, session: SessionDep):
#     db_hero = Hero.model_validate(hero)
#     session.add(db_hero)
#     session.commit()
#     session.refresh(db_hero)
#     return db_hero
#
#
# @app.get("/heroes/", response_model=list[HeroPublic])
# def read_heroes(
#     session: SessionDep,
#     offset: int = 0,
#     limit: Annotated[int, Query(le=100)] = 100,
# ):
#     heroes = session.exec(select(Hero).offset(offset).limit(limit)).all()
#     return heroes
#
#
# @app.get("/heroes/{hero_id}", response_model=HeroPublic)
# def read_hero(hero_id: int, session: SessionDep):
#     hero = session.get(Hero, hero_id)
#     if not hero:
#         raise HTTPException(status_code=404, detail="Hero not found")
#     return hero
#
#
# @app.patch("/heroes/{hero_id}", response_model=HeroPublic)
# def update_hero(hero_id: int, hero: HeroUpdate, session: SessionDep):
#     hero_db = session.get(Hero, hero_id)
#     if not hero_db:
#         raise HTTPException(status_code=404, detail="Hero not found")
#     hero_data = hero.model_dump(exclude_unset=True)
#     hero_db.sqlmodel_update(hero_data)
#     session.add(hero_db)
#     session.commit()
#     session.refresh(hero_db)
#     return hero_db
#
#
# @app.delete("/heroes/{hero_id}")
# def delete_hero(hero_id: int, session: SessionDep):
#     hero = session.get(Hero, hero_id)
#     if not hero:
#         raise HTTPException(status_code=404, detail="Hero not found")
#     session.delete(hero)
#     session.commit()
#     return {"ok": True}