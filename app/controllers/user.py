from fastapi import APIRouter, HTTPException, Depends, status
from app.schemas.user import UserInCreate
from app.services.user import AuthService
from app.models.user import User
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

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
        
    
    async def login(self, form_data: OAuth2PasswordRequestForm=Depends()):
        user = await AuthService.get_user_by_email(form_data.username)
        if not user or not AuthService.verify_password(form_data.password, user.hashed_password):
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid Credentials")
        access_token = await AuthService.create_access_token(data={"sub": user.email})
        return {
            "access_token": access_token,
            "token_type": "bearer"
        }