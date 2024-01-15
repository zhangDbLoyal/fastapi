from fastapi import APIRouter

user = APIRouter()

@user.get("/get",summary="this is a get method")
def get():
    return {"user":"get"}

@user.post("/post")
def get():
    return {"user":"post"}