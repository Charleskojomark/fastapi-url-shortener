from fastapi import HTTPException, status
from app.core.database import db
from app.models.url import URL
from app.utils.hash import generate_hash
from app.utils.redis import redis_client
from typing import Optional
import json
from bson import json_util

class URLService:
    async def shorten_url(self, original_url: str, base_url: str, user_id: Optional[str], custom_hash: Optional[str] = None) -> str:
        existing_data = {
            "original_url":original_url
        }
        existing_url = await db.urls.find_one(existing_data)
        short_hash = custom_hash or generate_hash(original_url, 6)
        existing_short = await db.urls.find_one({"short_hash": short_hash})
        
        if existing_url:
            existing_url = URL(**existing_url)
            return existing_url.short_url
        elif existing_short:
            raise HTTPException(status_code=status.HTTP_409_CONFLICT,detail="Custom url already exists.")
        
        short_url = f"{base_url}{short_hash}"
        data = {
            "original_url": original_url,
            "short_url": short_url,
            "short_hash": short_hash,
            "user_id": user_id,
            "clicks": 0
        }
        await db.urls.insert_one(data)
        return short_url
    
    async def get_url(self, short_hash: str) -> URL:
        # Try to fetch full URL data from Redis
        cached_data = await redis_client.get(short_hash)
        if cached_data:
            url_dict = json_util.loads(cached_data)
            return URL(**url_dict)

        # Fallback to DB
        url_data = await db.urls.find_one({"short_hash": short_hash})
        if not url_data:
            raise ValueError("URL not found")

        # Cache full JSON data
        
        await redis_client.set(short_hash, json_util.dumps(url_data), ex=3600)

        return URL(**url_data)
