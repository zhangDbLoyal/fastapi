
import uvicorn as uvicorn
from fastapi import FastAPI

app = FastAPI()



if __name__ == "__main__":
    uvicorn.run("main:app",port=8080,reload=True)

