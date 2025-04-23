import os
from motor.motor_asyncio import AsyncIOMotorClient
from dotenv import load_dotenv
from pymongo.errors import ConnectionFailure
load_dotenv()

client = AsyncIOMotorClient(os.getenv("MONGO_URI"))
db = client["url_shortener"]
urls_collection = db.urls 

async def create_indexes():
    await urls_collection.create_index([("short_url", 1)], unique=True)
    await urls_collection.create_index([("original_url", 1)], unique=True)
    await urls_collection.create_index([("short_hash", 1)], unique=True)

async def init_db():    
    await create_indexes()

