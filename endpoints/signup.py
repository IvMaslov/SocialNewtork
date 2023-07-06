from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse
from asyncpg.exceptions import UniqueViolationError
from typing import Union
from models.users import *
from models.general import Message
from .depends import get_user_repository

router = APIRouter()

@router.post("/", response_model=User, responses={400: {"model": Message}})
async def sign_up(
    user: UserIn,
    user_repository = Depends(get_user_repository)
    ) -> Union[User, JSONResponse]:

    try:
        response_obj = await user_repository.create(user)
    except UniqueViolationError:
        return JSONResponse(content={"message": "user already exists"},  status_code=400)
    else:
        return response_obj
