
from typing import Union
from models.users import UserIn, User
from db.postgres.users import users
from security.security import hash_password
from .base import BaseRepository

class UsersRepository(BaseRepository):
    
    async def create(self, u: UserIn) -> User:
        user = User(
            user_id=0,
            email=u.email,
            password=hash_password(u.password)
        )
        values = user.dict()
        values.pop("user_id", None)
        query = users.insert().values(**values)
        user.user_id = await self.database.execute(query=query)
        return user
    
    async def get_by_email(self, email: str) -> Union[User, None]:
        query = users.select().where(users.c.email==email)
        user = await self.database.fetch_one(query)
        if user is None:
            return None
        return User.parse_obj(user)