from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime, timezone

class URL(BaseModel):
    original_url: str = Field(..., description="The original long URL")
    short_url: str = Field(..., description="The shortened version of the original URL")
    short_hash: str = Field(..., description="The unique hash for the shortened URL")
    clicks: int = Field(default=0, description="Number of times the URL was visited")
    user_id: Optional[str] = None
    created_at: datetime = datetime.now(timezone.utc)
    
