from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse
from fastapi.security import OAuth2PasswordRequestForm
from typing_extensions import Annotated
from typing import Union
from models.general import Message
from models.token import Token
from repository.users import UsersRepository
from security.security import create_access_token, verify_password
from .depends import get_user_repository

router = APIRouter()


@router.post("/", response_model=Token, responses={400: {"model": Message}})
async def login(
        login: Annotated[OAuth2PasswordRequestForm, Depends()],
        user_repository: UsersRepository = Depends(get_user_repository)
    ) -> Union[Token, JSONResponse]:
    user = await user_repository.get_by_email(login.username)
    if user is None or not verify_password(login.password, user.password):
        return JSONResponse(content={"message": "wrong email or password"}, status_code=400)
    
    access_token = create_access_token({"sub": login.username})
    return Token.parse_obj({"access_token": access_token, "token_type": "bearer"})