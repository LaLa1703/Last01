from app.backend.db import Base, engine
from app.models.user import User
from app.models.task import Task


Base.metadata.create_all(bind=engine)

from sqlalchemy.schema import CreateTable

print(CreateTable(User.__table__).compile(engine))
print(CreateTable(Task.__table__).compile(engine))
