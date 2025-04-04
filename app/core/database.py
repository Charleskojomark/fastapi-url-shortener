import os
from motor.motor_asyncio import AsyncIOMotorClient
from dotenv import load_dotenv
from pymongo.errors import ConnectionFailure
load_dotenv()

client = AsyncIOMotorClient(os.getenv("MONGO_URI"))
db = client.get_database()
urls_collection = db.urls 

def create_indexes():
    urls_collection.create_index([("short_url", 1)], unique=True)
    urls_collection.create_index([("original_url", 1)], unique=True)
    urls_collection.create_index([("short_hash", 1)], unique=True)
    
create_indexes()