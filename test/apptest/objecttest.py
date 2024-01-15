from fastapi import APIRouter
from pydantic import BaseModel,Field,validator
from datetime import date
from typing import List
object = APIRouter()

class address(BaseModel):
    name:str
    phone:str

class user (BaseModel):
    name:str
    age:int = Field(default=0,gt=-1,lt=100)
    date:date
    address:address

class people (BaseModel):
    user : List[user]

@object.post("/user")
def get_user(user:user):
    return user

@object.post("/people")
def get_user(people:people):
    return people.user
