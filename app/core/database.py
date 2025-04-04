import os
from pymongo import MongoClient
from dotenv import load_dotenv
from pymongo.errors import ConnectionFailure
load_dotenv()

client = MongoClient(os.getenv("MONGO_URI"))

try:
    client.admin.command("ping")
    print("Connected to mongodb")
except ConnectionFailure as e:
    print("failed to connect". e)