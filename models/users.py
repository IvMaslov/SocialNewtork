from typing import Optional
from pydantic import BaseModel, EmailStr

class User(BaseModel):
    user_id: int
    email: EmailStr
    password: str

class UserIn(BaseModel):
    email: EmailStr
    password: str