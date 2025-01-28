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


from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os

db_path = os.path.join(os.path.abspath(os.path.dirname(__file__)), "..", "taskmanager.db")
SQLALCHEMY_DATABASE_URL = f"sqlite:///{db_path}"

engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

