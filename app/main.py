from fastapi import FastAPI

from .database import init_db
from .routers import student

app = FastAPI()
app.include_router(student.router)


@app.on_event("startup")
async def start_db():
    await init_db()


@app.get("/", tags=["Root"])
async def root():
    return {"message": "Welcome to my FastAPI!"}
