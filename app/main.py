from fastapi import FastAPI
from .routers import basic

app = FastAPI()

app.include_router(basic.router)


@app.get("/")
def root():
    return {"root"}
