# from sqlalchemy import create_engine
# from sqlalchemy.orm import sessionmaker, DeclarativeBase
# from sqlalchemy import Column, Integer, String
#
# engine = create_engine('sqlite:///taskmanager.db', echo=True)
#
# SessionLocal = sessionmaker(bind=engine)
#
#
# class Basee(DeclarativeBase):
#     pass


from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker, declarative_base

DATABASE_URL = "sqlite:///taskmanager.db"

engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
