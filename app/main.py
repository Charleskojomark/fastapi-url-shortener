from fastapi import FastAPI
import uvicorn 
from app.routes.url import router as url_router
from app.routes.user import router as user_router
from app.core.database import init_db
from contextlib import asynccontextmanager


@asynccontextmanager
async def lifespan(app: FastAPI):
    await init_db()
    print("connected to db")
    yield

app = FastAPI(title="URL Shortener API", version="1.0.0", lifespan=lifespan)
app.include_router(url_router)
app.include_router(user_router, prefix="/auth")

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8080, reload=True)
