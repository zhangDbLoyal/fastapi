
import uvicorn as uvicorn
from fastapi import APIRouter
from typing import Union

aapp = APIRouter()


@aapp.get("/get/{id}",summary="this is a get method",description="this is discription",response_description="this is res_discription")
def start(id: Union[int,str],name:str = None,account:str = None):
    return {
        "aappget": id,
        "name":name,
        "account":account
            }



