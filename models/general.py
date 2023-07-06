from pydantic import BaseModel

class Message(BaseModel):
    message: str

class PostIdUserId(BaseModel):
    post_id: int
    user_id: int