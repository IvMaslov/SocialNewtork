import sqlalchemy
from .base import metadata

dislikes = sqlalchemy.Table(
    "dislikes",
    metadata,
    sqlalchemy.Column("post_id", sqlalchemy.ForeignKey("posts.post_id"), nullable=False),
    sqlalchemy.Column("user_id", sqlalchemy.ForeignKey("users.user_id"), nullable=False)
)