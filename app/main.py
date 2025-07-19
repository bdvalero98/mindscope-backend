from fastapi import FastAPI

from app.api import users

app = FastAPI(title="MindScope API")

app.include_router(users.router)


@app.get("/")
def read_root():
    return {"message": "MindScope backend is running"}
