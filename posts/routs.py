from typing import Optional

from fastapi import APIRouter, status, Depends

from common.schemas import MessageResponse, TokenData
from posts.schemas import PostRequest, PostCreateResponse
from posts.service.like_service import LikePostService
from posts.service.post_service import PostCRUDService
from users.services.auth import AuthUser

post_router = APIRouter(tags=["Post"], prefix="/post")
like_router = APIRouter(tags=["Like"], prefix="/like")


@post_router.post(
    "/v1/create", status_code=status.HTTP_201_CREATED, response_model=PostCreateResponse
)
def create_post(
    data: PostRequest,
    token: TokenData = Depends(AuthUser()),
    post_service: PostCRUDService = Depends(PostCRUDService),
):
    return post_service.create_post(data, token)


@like_router.post(
    "/v1/{post_id}", status_code=status.HTTP_201_CREATED, response_model=MessageResponse
)
def like_post(
    post_id: str,
    token: TokenData = Depends(AuthUser()),
    like_service: LikePostService = Depends(LikePostService),
):
    return like_service.like_post(post_id, token)


@like_router.delete("/v1/{post_id}/unlike", status_code=status.HTTP_204_NO_CONTENT)
def unlike_post(
    post_id: str,
    token: TokenData = Depends(AuthUser()),
    like_service: LikePostService = Depends(LikePostService),
):
    return like_service.unlike_post(post_id, token)


@like_router.get(
    "/v1/statistics", status_code=status.HTTP_200_OK, response_model=MessageResponse
)
def unlike_post(
    from_date: Optional[str] = None,
    to_date: Optional[str] = None,
    like_service: LikePostService = Depends(LikePostService),
    token: TokenData = Depends(AuthUser()),
):
    return like_service.like_count(from_date, to_date)
