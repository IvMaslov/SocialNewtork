from fastapi import FastAPI
from db.postgres.base import database
from endpoints import login, signup, posts, likes, dislikes

app = FastAPI()

app.include_router(login.router, prefix="/login", tags=["login"])
app.include_router(signup.router, prefix="/signup", tags=["signup"])
app.include_router(posts.router, prefix="/posts", tags=["posts"])
app.include_router(likes.router, prefix="/likes", tags=["likes"])
app.include_router(dislikes.router, prefix="/dislike", tags=["dislike"])


@app.on_event("startup")
async def on_startup():
    await database.connect()

@app.on_event("shutdown")
async def on_shutdown():
    await database.disconnect()