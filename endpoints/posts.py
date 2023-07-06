from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse
from typing_extensions import Annotated
from typing import Union
from pydantic.error_wrappers import ValidationError
from models.users import User
from models.posts import *
from models.general import Message
from security.auth import get_current_user
from repository.posts import PostsRepository
from .depends import get_posts_repository

router = APIRouter()


@router.get("/user", responses={401: {"model": Message}})
async def get_by_user(
        current_user: Annotated[User, Depends(get_current_user)],
        posts_repository: PostsRepository = Depends(get_posts_repository)
    ):
    return await posts_repository.get_by_user(current_user.user_id) # type: ignore


@router.get("/newests")
async def get_newests(
        page: int,
        current_user: Annotated[User, Depends(get_current_user)],
        posts_repository: PostsRepository = Depends(get_posts_repository)    
    ):
    if page < 1:
        page =  1
    return await posts_repository.get_newests(page)


@router.post("/create", response_model=Post, status_code=201, responses={401: {"model": Message}, 400: {"model": Message}})
async def create(
        post_in: PostIn,
        current_user: Annotated[User, Depends(get_current_user)],
        posts_repository: PostsRepository = Depends(get_posts_repository)
    ) -> Union[Post, JSONResponse]:
    if len(post_in.title) > 255:
        return JSONResponse(content={"message": "title too long"}, status_code=400)
    return await posts_repository.create(PostInner(user_id=current_user.user_id, title=post_in.title, text=post_in.text)) # type: ignore
    

@router.put("/update", response_model=Post, responses={401: {"model": Message}, 400: {"model": Message}})
async def update(
        post_in: PostUpdate,
        current_user: Annotated[User, Depends(get_current_user)],
        posts_repository: PostsRepository = Depends(get_posts_repository)
    ) -> Union[Post, JSONResponse]:
    if len(post_in.title) > 255:
        return JSONResponse(content={"message": "title too long"}, status_code=400)
    user_id = posts_repository.get_user_id(post_in.post_id)
    if user_id != current_user.user_id:
        return JSONResponse(content={"message": "access forbiden"}, status_code=403)
    return await posts_repository.update(Post(post_id=post_in.post_id, user_id=current_user.user_id, title=post_in.title, text=post_in.text, created_at=datetime.now())) # type: ignore


@router.delete("/delete", responses={401: {"model": Message}, 403: {"model": Message}, 200: {"model": Message}})
async def delete(
        post_id: int,
        current_user: Annotated[User, Depends(get_current_user)],
        posts_repository: PostsRepository = Depends(get_posts_repository)
    ) -> JSONResponse:
    try:
        user_id = await posts_repository.get_user_id(post_id=post_id)
    except ValidationError:
        return JSONResponse(content={"message": "access forbiden"}, status_code=403)
    if user_id != current_user.user_id:
        return JSONResponse(content={"message": "access forbiden"}, status_code=403)
    await posts_repository.delete(post_id=post_id)
    return JSONResponse(content={"message": "successfully deleted"})