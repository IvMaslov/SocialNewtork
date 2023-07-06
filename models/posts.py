from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class Post(BaseModel):
    post_id: Optional[int] = None
    user_id: int
    title: str
    text: str
    created_at: datetime

class PostInner(BaseModel):
    user_id: int
    title: str
    text: str

class PostUpdate(BaseModel):
    post_id: int
    title: str
    text: str

class PostIn(BaseModel):
    title: str
    text: str