from fastapi import APIRouter
from utils.jwt_manager import create_token,validate_token
from fastapi.responses import HTMLResponse, JSONResponse
from pydantic import BaseModel
from schemas.user import User
user_router = APIRouter()

@user_router.post('/login',tags=['auth'])
def login(user: User):
     if user.email == "admin@gmail.com" and user.password =="admin":
          token: str = create_token(user.dict())
          return JSONResponse(status_code = 200,content=token)
     return "no es epico papu"