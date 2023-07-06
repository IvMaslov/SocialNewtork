from repository.users import UsersRepository
from repository.posts import PostsRepository
from repository.likes import LikesRepository
from repository.dislikes import DislikesRepository
from db.postgres.base import database

def get_user_repository() -> UsersRepository:
    return UsersRepository(database=database)

def get_posts_repository() -> PostsRepository:
    return PostsRepository(database=database)

def get_likes_repository() -> LikesRepository:
    return LikesRepository(database=database)

def get_dislikes_repository() -> DislikesRepository:
    return DislikesRepository(database=database)