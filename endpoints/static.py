from fastapi import APIRouter
from fastapi.responses import FileResponse


router = APIRouter()

@router.get("/main")
def get_main():
    return FileResponse("static/main.html")

@router.get("/login")
def get_login():
    return FileResponse("static/login.html")

@router.get("/signup")
def get_signup():
    return FileResponse("static/signup.html")

@router.get("/myposts")
def get_myposts():
    return FileResponse("static/myposts.html")

@router.get("/index")
def get_index():
    return FileResponse("static/index.html")

@router.get("/create")
def get_create():
    return FileResponse("static/create.html")