from fastapi import Request, HTTPException, status
from fastapi.responses import RedirectResponse
from app.services.url import URLService
from app.schemas.url import URLRequest

class URLController:
    def __init__(self, url_service: URLService):
        self.url_service = url_service
    
    async def shorten_url(self, request: Request, url_request: URLRequest):
        base_url = str(request.base_url)
        original_url = url_request.original_url
        short_url = await self.url_service.shorten_url(original_url, base_url)
        data = {
            "shortened_url": short_url
        }
        return data
    
    async def get_url(self, short_url: str) -> str:
        try:
            url = await self.url_service.get_url(short_url)
            return(RedirectResponse(url.original_url))
        except ValueError:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="URL NOT FOUND")