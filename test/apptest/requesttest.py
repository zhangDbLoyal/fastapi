from fastapi import APIRouter,Request
from pydantic import BaseModel,Field,validator
from datetime import date
from typing import List
request = APIRouter()


@request.post("/request")
def get_request(request:Request):
    return {
        "client":request.client,
        "headers": request.headers,
        "url": request.url,
        "cookies": request.cookies,
    }
