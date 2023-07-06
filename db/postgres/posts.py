import sqlalchemy
from .base import metadata

posts = sqlalchemy.Table(
    "posts",
    metadata,
    sqlalchemy.Column("post_id", sqlalchemy.Integer, primary_key=True, autoincrement=True),
    sqlalchemy.Column("user_id", sqlalchemy.ForeignKey("users.user_id", ondelete="CASCADE"), nullable=False),
    sqlalchemy.Column("title", sqlalchemy.String, nullable=False),
    sqlalchemy.Column("text", sqlalchemy.Text, nullable=False),
    sqlalchemy.Column("created_at", sqlalchemy.DateTime)
)