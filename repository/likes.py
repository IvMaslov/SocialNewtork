
from db.postgres.likes import likes
from models.general import PostIdUserId
from .base import BaseRepository


class LikesRepository(BaseRepository):

    async def create(self, like_info: PostIdUserId):
        values = like_info.dict()
        query = likes.insert().values(**values)
        return await self.database.execute(query=query)
    
    async def get_like(self, like_info: PostIdUserId):
        query = likes.select().where(likes.c.post_id==like_info.post_id, likes.c.user_id==like_info.user_id)
        return await self.database.fetch_one(query=query)
    
    async def delete(self, like_info: PostIdUserId) -> None:
        query = likes.delete().where(likes.c.post_id==like_info.post_id, likes.c.user_id==like_info.user_id)
        return await self.database.execute(query=query)