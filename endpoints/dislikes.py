from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse
from typing_extensions import Annotated
from models.users import User
from models.general import Message
from security.auth import get_current_user
from repository.posts import PostsRepository
from db.redis.client import redis_client
from .depends import get_posts_repository

router = APIRouter()


@router.post("/", responses={400: {"model": Message}})
async def dislike(
        post_id: int,
        current_user: Annotated[User, Depends(get_current_user)],
        posts_repository: PostsRepository = Depends(get_posts_repository)
    ):
    post_author_id = await posts_repository.get_user_id(post_id=post_id)
    if post_author_id == current_user.user_id:
        return JSONResponse(content={"message": "dislike yourself is not allowed"}, status_code=400)
    
    post_match = "{}:{}".format(post_id, current_user.user_id)
    
    exists = redis_client.sismember("dislikes", post_match)
    if exists:
        redis_client.srem("dislikes", post_match)
        return JSONResponse(content={"message": "dislike was deleted"})
    
    like = redis_client.sismember("likes", post_match)
    if like:
        redis_client.srem("likes", post_match)

    redis_client.sadd("dislikes", post_match)
    return JSONResponse(content={"message": "success"}, status_code=200)