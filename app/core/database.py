import os
from motor.motor_asyncio import AsyncIOMotorClient
from dotenv import load_dotenv
from pymongo.errors import ConnectionFailure
load_dotenv()

client = AsyncIOMotorClient(os.getenv("MONGO_URI"))
db = client["url_shortener"]

