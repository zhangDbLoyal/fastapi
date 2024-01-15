from fastapi import APIRouter,Response
from pydantic import BaseModel,Field,validator
from datetime import date
from typing import List
aresponse = APIRouter()



class user (BaseModel):
    name:str = "A"
    age:int = None
    date:date
    phont : int

class user_out (BaseModel):
    name:str
    age:int



@aresponse.post("/get_responses",response_model=user)
def get_aresponses():
    # return user
    return {
        "date": "2000-02-05"
    }
# @aresponse.post("/get_response_model_exclude_defaults",response_model_exclude_defaults=True)
# def get_aresponse_model_exclude_defaults(user:user):
#     return user
@aresponse.post("/unset",response_model=user,response_model_exclude_unset=True)
def get_unset():
    return {
        "date":"2000-02-05"
    }
@aresponse.post("/none",response_model=user,response_model_exclude_none=True)
def get_none():
    return user
@aresponse.post("/default",response_model=user,response_model_exclude_defaults=True)
def get_default(user:user):
    return user

@aresponse.post("/include",response_model=user,response_model_include="name")
def get_default(user:user):
    return user



