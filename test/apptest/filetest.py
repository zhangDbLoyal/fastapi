import os

from fastapi import APIRouter,Form,File,UploadFile
from pydantic import BaseModel,Field,validator
from datetime import date
from typing import List
file = APIRouter()


@file.post("/file")
def get_len(file : bytes = File()):
    return {
        "len":len(file)
    }

@file.post("/bigfile")
def get_name(files : List[UploadFile]):
    file_names = {}
    for file in files:
        path = os.path.join("apptest\\img", file.filename)
        path = os.path.abspath(path)
        # path.replace("\\",'/')
        print("1" + path)
        with open(path, "wb") as f:
            for line in file.file:
                f.write(line)
        file_names[file.filename[0:3]] = file.filename
    return file_names