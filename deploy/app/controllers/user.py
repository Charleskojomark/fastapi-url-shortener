from fastapi import APIRouter, HTTPException, Depends, status, Request
from app.schemas.user import UserInCreate, LoginRequest
from app.services.user import AuthService
from app.models.user import User
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from typing import Annotated

router = APIRouter()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="auth/login")

class AuthController:
    
    async def register(self, user: UserInCreate):
        existing_email = await AuthService.get_user_by_email(user.email)
        existing_username = await AuthService.get_user_by_username(user.username)
        if existing_email:
            raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="Email already exists")
        elif existing_username:
            raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="Username already exists")
        new_user = await AuthService.create_user(user)
        return {
            "message": "user registered successfully",
            "user": {
                new_user["username"],
                new_user["email"]
            }
        }
        
    
    async def login(self, request: Request):
        login_data: LoginRequest = await AuthService.parse_login_input(request)
        
        user = await AuthService.get_user_by_username(login_data.username_or_email)
        if not user:
            user = await AuthService.get_user_by_email(login_data.username_or_email)
        if not user:
            raise HTTPException(status_code=401, detail="Invalid Credentials")
        if not AuthService.verify_password(login_data.password, user.hashed_password):
            raise HTTPException(status_code=401, detail="Invalid Credentials")
        token = AuthService.create_access_token({"sub": user.email})
        return {
            "access_token": token,
            "token_type": "bearer"
        }
        