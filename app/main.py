from fastapi import FastAPI
import uvicorn 
from routes.url import router as url_router

app = FastAPI(title="URL Shortener API", version="1.0.0")

app.include_router(url_router)

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8080, reload=True)
