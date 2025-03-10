from fastapi import FastAPI


app = FastAPI()

@app.get('/')
async def root():
    return {'message': 'Главная страница'}

@app.get('/user/admin')
async def user_admin():
    return {'message': 'Вы вошли как администратор'}

@app.get('/user/{user_id}')
async def user_id(user_id: int):
    return {'message': f'Вы вошли как пользователь № {user_id}'}

@app.get('/user')
async def id_paginator(username: str, age: int) -> dict:
    return {'message': f'Информация о пользователе. Имя: {username}, Возраст:{age}'}

