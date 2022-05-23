from fastapi import Depends, APIRouter, status, Request

from common.schemas import MessageResponse, LoginResponse, TokenData
from users.schemas import CreateUserRequest, LoginUser, LastVisitResponse
from users.services.auth import AuthUser
from users.services.login import LoginService
from users.services.user_service import UserCRUDService

user_router = APIRouter(tags=["User"], prefix="/user")


@user_router.post(
    "/v1/signup", status_code=status.HTTP_201_CREATED, response_model=MessageResponse
)
def signup_user(
    request: CreateUserRequest,
    user_service: UserCRUDService = Depends(UserCRUDService),
):
    return user_service.create_user(request)


@user_router.post(
    "/v1/login", status_code=status.HTTP_200_OK, response_model=LoginResponse
)
def login_user(
    request: Request, data: LoginUser, login_service: LoginService = Depends(LoginService)
):
    return login_service.login(data, request.url)


@user_router.get(
    "/v1/last-activity", status_code=status.HTTP_200_OK, response_model=LastVisitResponse
)
def last_activity_user(
    token: TokenData = Depends(AuthUser()),
    user_service: UserCRUDService = Depends(UserCRUDService),
):
    return user_service.last_activity(token.user_id)


@user_router.get(
    "/v1/last-activity-by-id/{user_id}", status_code=status.HTTP_200_OK, response_model=LastVisitResponse
)
def last_activity_user(
    user_id: str,
    user_service: UserCRUDService = Depends(UserCRUDService),
):
    return user_service.last_activity(user_id)
