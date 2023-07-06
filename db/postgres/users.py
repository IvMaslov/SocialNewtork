import sqlalchemy
from .base import metadata

users = sqlalchemy.Table(
    "users",
    metadata,
    sqlalchemy.Column("user_id", sqlalchemy.Integer, primary_key=True, autoincrement=True),
    sqlalchemy.Column("email", sqlalchemy.String, unique=True),
    sqlalchemy.Column("password", sqlalchemy.String)
)