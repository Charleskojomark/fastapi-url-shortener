from fastapi import FastAPI

app = FastAPI(title="URL Shortener API", version="1.0.0")

@app.get("/")
async def read_root() -> dict:
    return {"message": "Welcome to FastAPI URL shortener"}
