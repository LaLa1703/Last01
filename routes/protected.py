from fastapi import APIRouter, HTTPException, Depends
from fastapi.security import OAuth2PasswordBearer
from auth.jwt_handler import verify_token

router = APIRouter()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")


@router.get("/protected")
def protected_route(token: str = Depends(oauth2_scheme)):
    payload = verify_token(token)
    if not payload:
        raise HTTPException(status_code=401, detail="Недействительный токен")

    return {"message": f"Доступ разрешен для {payload['role']}"}
