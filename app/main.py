from fastapi import FastAPI

from .routers import hello

app = FastAPI()
app.include_router(hello.router, prefix="/hello")


@app.get("/")
async def ping():
    return {"ping": "ok"}
