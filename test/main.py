
import uvicorn as uvicorn
from fastapi import FastAPI
from apptest.UserTest import user
from AppTest import aapp
from apptest.objecttest import object
from apptest.formtest import form
from apptest.filetest import file
from apptest.requesttest import request
from apptest.responsetest import aresponse
from fastapi.staticfiles import StaticFiles
app = FastAPI()
# app.mount("/static",StaticFiles(directory="apptest/img"))
app.include_router(user,prefix="/user",tags=["userTest"])
app.include_router(aapp,prefix="/app",tags=["appTest"])
app.include_router(object,prefix="/object",tags=["objectTest"])
app.include_router(form,prefix="/form",tags=["formtest"])
app.include_router(file,prefix="/file",tags=["filetest"])
app.include_router(request,prefix="/request",tags=["requesttest"])
app.include_router(aresponse,prefix="/response",tags=["responsetest"])


@app.get("/")
def start():
    return {"Hello": "World"}


if __name__ == "__main__":
    uvicorn.run("main:app",port=8080,reload=True)

