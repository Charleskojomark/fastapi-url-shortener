from pydantic import BaseModel, EmailStr

class User(BaseModel):
    username: str
    email: EmailStr

class UserInCreate(User):
    password: str

class UserInDB(User):
    hashed_password: str

        
class LoginRequest(BaseModel):
    username_or_email: str
    password: str
    

class Token(BaseModel):
    access_token: str
    token_type: str
    
class TokenData(BaseModel):
    email: str | None = None