from pydantic import BaseModel

class UserInCreate(BaseModel):
    username: str
    email: str
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
    email: str
    hashed_password: str

    class Config:
        json_schema_extra = {
            "example": {
                "username": "john_doe",
                "email": "john@example.com",
                "hashed_password": "hashedpassword123456"
            }
        }