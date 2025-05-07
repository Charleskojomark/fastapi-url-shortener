# schemas/url.py
from pydantic import BaseModel
from typing import Optional

class URLRequest(BaseModel):
    original_url: str
    custom_alias: Optional[str] = None
