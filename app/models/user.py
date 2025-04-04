from pydantic import BaseModel

class User(BaseModel):
    username: str
    email: str
    hashed_password: str  # Store the hashed password

    class Config:
        # You can include extra fields or modify the schema representation
        json_schema_extra = {
            "example": {
                "username": "john_doe",
                "email": "john@example.com",
                "hashed_password": "hashedpassword123456"
            }
        }
        