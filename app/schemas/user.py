from pydantic import BaseModel, EmailStr

class UserInCreate(BaseModel):
    username: str
    email: EmailStr
    password: str

    class Config:
        json_schema_extra = {
            "example": {
                "username": "john_doe",
                "email": "john@example.com",
                "password": "strongpassword123"
            }
        }

class UserInDB(BaseModel):
    username: str
    email: EmailStr
    hashed_password: str

    class Config:
        json_schema_extra = {
            "example": {
                "username": "john_doe",
                "email": "john@example.com",
                "hashed_password": "hashedpassword123456"
            }
        }
        
class LoginRequest(BaseModel):
    username: str
    password: str