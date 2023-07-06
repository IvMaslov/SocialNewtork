from repository.users import UsersRepository
from repository.posts import PostsRepository
from db.postgres.base import database

def get_user_repository() -> UsersRepository:
    return UsersRepository(database=database)

def get_posts_repository() -> PostsRepository:
    return PostsRepository(database=database)
