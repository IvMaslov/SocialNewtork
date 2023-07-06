from fastapi.security import OAuth2PasswordBearer
from fastapi import status, Depends
from fastapi.responses import JSONResponse
from typing import Union
from typing_extensions import Annotated
from models.users import User
from repository.users import UsersRepository
from .security import decode_access_token
from endpoints.depends import get_user_repository


oauth2_bearer = OAuth2PasswordBearer(tokenUrl="/login")


async def get_current_user(token: Annotated[str, Depends(oauth2_bearer)], user_repository: UsersRepository = Depends(get_user_repository)) -> Union[User, JSONResponse]:
    credentials_exception = JSONResponse(
        status_code=status.HTTP_401_UNAUTHORIZED,
        content={"message": "could not validate credentials"},
        headers={"WWW-Authenticate": "Bearer"},
    )
    payload = decode_access_token(token)
    email = payload.get("sub")
    if email is None:
        return credentials_exception
    user = await user_repository.get_by_email(email)
    if user is None:
        return credentials_exception
    
    return user
    