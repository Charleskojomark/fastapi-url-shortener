from fastapi import APIRouter, Request
from app.controllers.url import URLController
from app.services.url import URLService

url_service = URLService()
url_controller = URLController(url_service)

router = APIRouter()

router.add_api_route("/v1/shorten", url_controller.shorten_url_v1, methods=["POST"]) # non-authenticated users
router.add_api_route("/v2/shorten", url_controller.shorten_url_v2, methods=["POST"]) # authenticated users
router.add_api_route("/{short_url}", url_controller.get_url, methods=["GET"])