from fastapi import Depends, HTTPException, status
from sqlalchemy.orm import Session

from common.default_message import DATA_NOT_FOUND, INVALID_DATA
from common.models import generate_current_date
from common.schemas import MessageResponse, TokenData
from common.validators import datatime_validator
from posts.models import PostLikeModel
from settings import get_db


class LikePostService:
    def __init__(
        self,
        db: Session = Depends(get_db),
    ):
        self._db = db

    def like_post(self, post_id: str, token: TokenData):
        try:
            like_obj = PostLikeModel(user_id=token.user_id, post_id=post_id)
            self._db.add(like_obj)
            self._db.commit()
        except Exception:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, detail=DATA_NOT_FOUND
            )
        return MessageResponse(**{"message": "Like"})

    def unlike_post(self, post_id: str, token: TokenData):
        liked_post = (
            self._db.query(PostLikeModel)
            .filter(
                PostLikeModel.post_id == post_id
                and PostLikeModel.user_id == token.user_id
            )
            .first()
        )
        if not liked_post:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, detail=DATA_NOT_FOUND
            )
        self._db.delete(liked_post)
        return self._db.commit()

    def like_count(self, from_date, to_date):
        try:
            if not from_date:
                from_date = datatime_validator(generate_current_date())
                query_like = self._db.query(PostLikeModel).filter(
                    PostLikeModel.created_at >= from_date
                )
            else:
                from_date = datatime_validator(from_date)
                query_like = self._db.query(PostLikeModel).filter(
                    PostLikeModel.created_at >= from_date
                )
            if to_date:
                datetime_object = datatime_validator(to_date)
                to_date = datetime_object
                query_like = query_like.filter(PostLikeModel.created_at <= to_date)
            result = query_like.count()
        except Exception:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST, detail=INVALID_DATA
            )
        return MessageResponse(**{"message": result})
