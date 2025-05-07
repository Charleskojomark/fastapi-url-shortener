from fastapi import APIRouter, Request
from app.controllers.user import AuthController
from app.services.user import AuthService

auth_controller = AuthController()

router = APIRouter()
router.add_api_route("/register", auth_controller.register, methods=["POST"])
router.add_api_route("/login", auth_controller.login, methods=["POST"])