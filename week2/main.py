import uvicorn
from fastapi import FastAPI
from es.basic import basic
from es.search import search
from vector.basic import v_basic
from fast_dfs.basic import f_basic
from fastapi.staticfiles import StaticFiles

app = FastAPI()
# app.mount("/static",StaticFiles(directory="apptest/img"))
app.include_router(basic,prefix="/basic",tags=["ESBasic"])
app.include_router(search,prefix="/search",tags=["ESSearch"])
app.include_router(v_basic,prefix="/vector",tags=["VectorBasic"])
app.include_router(f_basic,prefix="/fastdfs",tags=["FastdfsBasic"])


@app.get("/")
def start():
    return {"Hello": "World"}


if __name__ == "__main__":
    uvicorn.run("main:app",port=8081,reload=True)

