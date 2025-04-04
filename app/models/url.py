from pydantic import BaseModel, Field


class URL(BaseModel):
    original_url: str = Field(..., description="The original long URL")
    short_url: str = Field(..., description="The shortened version of the original URL")
    short_hash: str = Field(..., description="The unique hash for the shortened URL")
    clicks: int = Field(default=0, description="Number of times the URL was visited")

    model_config = {
        "json_schema_extra": {
            "example": {
                "original_url": "https://www.example.com/some/very/long/path",
                "short_url": "https://sho.rt/abc123",
                "short_hash": "abc123",
                "clicks": 42
            }
        }
    }
