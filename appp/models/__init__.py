from appp.backend.db import Base, engine
from appp.models.user import User
from appp.models.task import Task


Base.metadata.create_all(bind=engine)

from sqlalchemy.schema import CreateTable

print(CreateTable(User.__table__).compile(engine))
print(CreateTable(Task.__table__).compile(engine))
