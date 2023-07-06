from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse
from typing_extensions import Annotated
from models.users import User
from models.general import Message, PostIdUserId
from security.auth import get_current_user
from repository.likes import LikesRepository
from repository.dislikes import DislikesRepository
from repository.posts import PostsRepository
from db.redis.client import redis_client
from .depends import get_likes_repository, get_dislikes_repository, get_posts_repository

router = APIRouter()


@router.post("/", responses={400: {"model": Message}})
async def like(
        post_id: int,
        current_user: Annotated[User, Depends(get_current_user)],
        likes_repository: LikesRepository = Depends(get_likes_repository),
        dislikes_repository: DislikesRepository = Depends(get_dislikes_repository),
        posts_repository: PostsRepository = Depends(get_posts_repository)
    ):
    post_author_id = await posts_repository.get_user_id(post_id=post_id)
    if post_author_id == current_user.user_id:
        return JSONResponse(content={"message": "like yourself is not allowed"}, status_code=400)
    
    post_match = "{}:{}".format(post_id, current_user.user_id)
    
    exists = redis_client.sismember("likes", post_match)
    if exists:
        redis_client.srem("likes", post_match)
        return JSONResponse(content={"message": "like was deleted"})
    
    dislike = redis_client.sismember("dislikes", post_match)
    if dislike:
        redis_client.srem("dislikes", post_match)

    redis_client.sadd("likes", post_match)
    return JSONResponse(content={"message": "success"}, status_code=200)
    
    already_exists = await likes_repository.get_like(PostIdUserId(post_id=post_id, user_id=current_user.user_id))
    if not already_exists is None:
        await likes_repository.delete(PostIdUserId(post_id=post_id, user_id=current_user.user_id))
        return JSONResponse(content={"message": "like was deleted"})

    dislike = await dislikes_repository.get_dislike(PostIdUserId(post_id=post_id, user_id=current_user.user_id))
    if not dislike is None:
        await dislikes_repository.delete(PostIdUserId(post_id=post_id, user_id=current_user.user_id))

    return await likes_repository.create(PostIdUserId(post_id=post_id, user_id=current_user.user_id))