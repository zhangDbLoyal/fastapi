from fastapi import APIRouter,Form
from pydantic import BaseModel,Field,validator
from datetime import date
from typing import List
form = APIRouter()


@form.post("/login")
def get_user(username:str = Form(),password :str = Form()):
    return {
        "username":username
    }
