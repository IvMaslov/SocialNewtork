from passlib.context import CryptContext
import datetime
from jose import jwt
from jose.exceptions import JWTError
from config.config import app_config

SECRET_KEY = app_config["security"]["secret_key"]
ALGORITHM = app_config["security"]["algorithm"]
TOKEN_EXPIRES = app_config["security"]["token_expires"]

crypt_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def verify_password(password: str, hash: str) -> bool:
    return crypt_context.verify(password, hash)

def hash_password(password: str) -> str:
    return crypt_context.hash(password)

def create_access_token(data: dict) -> str:
    to_encode = data.copy()
    to_encode.update({"exp": datetime.datetime.utcnow() + datetime.timedelta(minutes=TOKEN_EXPIRES)})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

def decode_access_token(token: str) -> dict:
    try:
        decoded_jwt = jwt.decode(token,SECRET_KEY,algorithms=[ALGORITHM])
    except JWTError:
        return {}
    return decoded_jwt
