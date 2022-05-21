from fastapi import Depends, HTTPException, status
from sqlalchemy.orm import Session

from common.default_message import INVALID_DATA, POST_CREATED
from common.schemas import TokenData
from posts.models import PostModel
from posts.schemas import PostRequest, PostCreateResponse
from settings import get_db


class PostCRUDService:
    def __init__(
        self,
        db: Session = Depends(get_db),
    ):
        self._db = db

    def create_post(self, data: PostRequest, token: TokenData):
        try:
            post_data = {
                "user_id": token.user_id,
                "header": data.header,
                "text": data.text,
            }
            post_obj = PostModel(**post_data)
            self._db.add(post_obj)
            self._db.commit()
        except Exception:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST, detail=INVALID_DATA
            )
        return PostCreateResponse(
            **{"message": POST_CREATED, "post_id": str(post_obj.id)}
        )
