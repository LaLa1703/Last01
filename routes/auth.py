from fastapi import APIRouter, HTTPException, Depends
from fastapi.security import OAuth2PasswordBearer
from auth.jwt_handler import create_token, verify_token
from auth.redis_handler import redis_client
from models.user import User

router = APIRouter()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

users_db = {
    "admin": {"password": "admin123", "role": "admin"},
    "user": {"password": "user123", "role": "user"}
}


@router.post("/login")
def login(user: User):
    if user.username not in users_db or users_db[user.username]["password"] != user.password:
        raise HTTPException(status_code=401, detail="Неверные учетные данные")

    role = users_db[user.username]["role"]
    token = create_token(user_id=user.username, role=role)
    return {"access_token": token}


@router.post("/logout")
def logout(token: str = Depends(oauth2_scheme)):
    redis_client.set(token, "blacklisted", ex=3600)
    return {"message": "Вы вышли"}
