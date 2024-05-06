from typing import List
from db.postgres.posts import posts
from sqlalchemy import desc
from models.posts import *
from .base import BaseRepository

class PostsRepository(BaseRepository):

    async def create(self, p: PostInner) -> Post:
        post = Post(
            user_id=p.user_id,
            title=p.title, 
            text=p.text,
            created_at=datetime.now()
        )
        values = post.dict()
        values.pop("post_id")
        query = posts.insert().values(**values)
        post.post_id = await self.database.execute(query=query)
        return post
    
    async def update(self, p: Post) -> Post:
        values = p.dict()
        query = posts.update().where(posts.c.post_id==p.post_id).values(**values)
        await self.database.execute(query=query)
        return p
    
    async def delete(self, post_id: int):
        query = posts.delete().where(posts.c.post_id==post_id)
        await self.database.execute(query=query)
    
    async def get_user_id(self, post_id: int) -> int:
        query = posts.select().where(posts.c.post_id==post_id)
        resp = await self.database.fetch_one(query=query)
        return Post.parse_obj(resp).user_id

    async def get_by_user(self, user_id: int) -> List:
        query = posts.select().where(posts.c.user_id==user_id)
        return await self.database.fetch_all(query=query) 
    
    async def get_newests(self, page: int):
        start = 12*(page-1)
        query = posts.select().order_by(desc(posts.c.created_at)).limit(12).offset(start)
        return await self.database.fetch_all(query=query)
    
    async def get_by_id(self, post_id: int):
        query = posts.select().where(posts.c.post_id==post_id)
        return await self.database.fetch_one(query=query)