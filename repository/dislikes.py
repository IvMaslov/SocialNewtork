
from db.postgres.dislikes import dislikes
from models.general import PostIdUserId
from .base import BaseRepository


class DislikesRepository(BaseRepository):

    async def create(self, like_info: PostIdUserId):
        values = like_info.dict()
        query = dislikes.insert().values(**values)
        return await self.database.execute(query=query)
    
    async def get_dislike(self, like_info: PostIdUserId):
        query = dislikes.select().where(dislikes.c.post_id==like_info.post_id, dislikes.c.user_id==like_info.user_id)
        return await self.database.fetch_one(query=query)
    
    async def delete(self, like_info: PostIdUserId):
        query = dislikes.delete().where(dislikes.c.post_id==like_info.post_id, dislikes.c.user_id==like_info.user_id)
        return await self.database.execute(query=query)