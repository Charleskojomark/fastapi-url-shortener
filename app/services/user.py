import os
import jwt
import datetime
from fastapi import Request, HTTPException, Depends, status
from fastapi.security import OAuth2PasswordBearer
from jwt.exceptions import InvalidTokenError
from passlib.hash import pbkdf2_sha256
from app.models.user import User
from app.core.database import db
from app.schemas.user import UserInCreate, LoginRequest, Token, TokenData
from typing import Optional, Annotated
from dotenv import load_dotenv
load_dotenv()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="auth/login")

class AuthService:
    
    @staticmethod
    def hash_password(password: str) -> str:
        return pbkdf2_sha256.hash(password)
    
    @staticmethod
    def verify_password(plain_password: str, hashed_password: str) -> bool:
        return pbkdf2_sha256.verify(plain_password, hashed_password)

    @staticmethod
    def create_access_token(data: dict) -> str:
        SECRET_KEY = os.getenv("SECRET_KEY")
        ALGORITHM = os.getenv("ALGORITHM")
        to_encode = data.copy()
        expire = datetime.datetime.now() + datetime.timedelta(minutes=int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES")))
        to_encode.update({"exp": expire})
        encoded_jwt = jwt.encode(to_encode, SECRET_KEY, ALGORITHM)
        return encoded_jwt
    
    @staticmethod
    async def get_user_by_email(email: str) -> Optional[User]:
        email_data = {"email": email}
        user_data = await db.users.find_one(email_data)
        if user_data:
            return User(**user_data)
        return None
    
    @staticmethod
    async def get_user_by_username(username: str) -> Optional[User]:
        username_data = {"username": username}
        user_data = await db.users.find_one(username_data)
        if user_data:
            return User(**user_data)
        return None
    
    
    
    @staticmethod
    async def create_user(user: UserInCreate) -> User:
        hashed_password = AuthService.hash_password(user.password)
        new_user = {
            "username": user.username,
            "email": user.email,
            "hashed_password": hashed_password
        }
        await db.users.insert_one(new_user)
        return new_user
        
    @staticmethod
    async def parse_login_input(request: Request) -> LoginRequest:
        content_type = request.headers.get("Content-Type", "")

        if "application/json" in content_type:
            try: 
                body = await request.json()
            except Exception:
                raise HTTPException(status_code=400, detail="Invalid JSON body")

            identifier = body.get("username") or body.get("email")
            if not identifier or "password" not in body:
                raise HTTPException(status_code=400, detail="Missing credentials")

            return LoginRequest(username_or_email=identifier, password=body["password"])

        elif "application/x-www-form-urlencoded" in content_type:
            form = await request.form()
            identifier = form.get("username") or form.get("email")
            if not identifier or "password" not in form:
                raise HTTPException(status_code=400, detail="Missing credentials")

            return LoginRequest(username_or_email=identifier, password=form["password"])

        raise HTTPException(status_code=415, detail="Unsupported Content-Type")
    
    @staticmethod        
    async def get_current_user(token: Annotated[Optional[str], Depends(oauth2_scheme)]) -> User:
        credentials_exception = HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Could not validate credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )
        try:
            payload = jwt.decode(token, os.getenv("SECRET_KEY"), algorithms=[os.getenv("ALGORITHM")])
            email = payload.get("sub")
            if email is None:
                raise credentials_exception
            token_data = TokenData(email=email)
        except InvalidTokenError:
            raise credentials_exception
        user_data = await db.users.find_one({"email": email})
        if user_data is None:
            raise credentials_exception
        return User(**user_data)
    