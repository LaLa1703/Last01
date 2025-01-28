import logging
import sys
import os
from fastapi import FastAPI
from app.routers.user import router as user_router
from app.routers.task import router as task_router

sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))

logging.basicConfig(level=logging.INFO)

app = FastAPI()

@app.get('/')
async def welcome():
    return {'message': 'Welcome to Taskmanager'}

app.include_router(user_router, prefix='/user')
app.include_router(task_router, prefix='/task')

