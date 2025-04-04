# schemas/url.py
from pydantic import BaseModel

class URLRequest(BaseModel):
    original_url: str
