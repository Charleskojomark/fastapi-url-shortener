from core.database import db
from models.url import URL
from utils.hash import generate_hash

class URLService:
    async def shorten_url(self, original_url: str, base_url: str) -> str:
        existing_data = {
            "original_url":original_url
        }
        existing_url = await db.urls.find_one(existing_data)
        if existing_url:
            existing_url = URL(**existing_url)
            return existing_url.short_url
        
        short_hash = generate_hash(original_url, 6)
        short_url = f"{base_url}{short_hash}"
        data = {
            "original_url": original_url,
            "short_url": short_url,
            "short_hash": short_hash
        }
        await db.urls.insert_one(data)
        return short_url
    
    async def get_url(self, short_hash: str) -> URL:
        data = {
            "short_hash": short_hash
        }
        url_data = await db.urls.find_one(data)
        if not url_data:
            raise ValueError("URL not found")
        return URL(**url_data)