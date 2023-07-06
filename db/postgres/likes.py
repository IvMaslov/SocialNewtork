import sqlalchemy
from .base import metadata

likes = sqlalchemy.Table(
    "likes",
    metadata,
    sqlalchemy.Column("post_id", sqlalchemy.ForeignKey("posts.post_id"), nullable=False),
    sqlalchemy.Column("user_id", sqlalchemy.ForeignKey("users.user_id"), nullable=False)
)