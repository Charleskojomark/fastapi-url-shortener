import os
import jwt
import datetime
from passlib.hash import pbkdf2_sha256
from models.user import User
from core.database import db
from schemas.user import UserInCreate
from typing import Optional
from dotenv import load_dotenv
load_dotenv()

class AuthService:
    
    def hash_password(self, password: str) -> str:
        return pbkdf2_sha256.hash(password)
    
    @staticmethod
    def verify_password(plain_password: str, hashed_password: str) -> str:
        return pbkdf2_sha256(plain_password, hashed_password)

    @staticmethod
    def create_access_token(data: dict) -> str:
        SECRET_KEY = os.getenv("SECRET_KEY")
        ALGORITHM = os.getenv("ALGORITHM")
        to_encode = data.copy()
        expire = datetime.datetime.now() + datetime.timedelta(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES"))
        to_encode.update({"exp": expire})
        encoded_jwt = jwt.encode(to_encode, SECRET_KEY, ALGORITHM)
        return encoded_jwt
    
    @staticmethod
    def get_user_by_email(email: str) -> User:
        email_data = {
            "email": email
        }
        user_data = db.users.find_one(email_data)
        if not user_data:
            raise ValueError("User Not found")
        return User(**user_data)
    
    def create_user(self, user: UserInCreate) -> User:
        hashed_password = self.hash_password(user.password)
        new_user = {
            "user_name": user.username,
            "email": user.email,
            "hashed_password": hashed_password
        }
        db.users.insert_one(new_user)
        return new_user
        