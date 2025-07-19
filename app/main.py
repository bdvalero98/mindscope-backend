from fastapi import FastAPI

app = FastAPI(title="MindScope API")

@app.get("/")
def read_root():
    return {"message": "MindScope backend is running"}