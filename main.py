from fastapi import FastAPI
from db.postgres.base import database
from endpoints import login, signup, posts, likes, dislikes, static

app = FastAPI()

app.include_router(login.router, prefix="/api/login", tags=["login"])
app.include_router(signup.router, prefix="/api/signup", tags=["signup"])
app.include_router(posts.router, prefix="/api/posts", tags=["posts"])
app.include_router(likes.router, prefix="/api/likes", tags=["likes"])
app.include_router(dislikes.router, prefix="/api/dislike", tags=["dislike"])
app.include_router(static.router, prefix="", tags=["main"])


@app.on_event("startup")
async def on_startup():
    await database.connect()

@app.on_event("shutdown")
async def on_shutdown():
    await database.disconnect()