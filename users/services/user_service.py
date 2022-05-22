from fastapi import Depends, HTTPException, status
from sqlalchemy.orm import Session

from common.default_message import (
    USER_ALREADY_EXISTS,
    REGISTRATION_SUCCESS,
    DATA_NOT_FOUND,
)
from common.schemas import MessageResponse, TokenData
from common.service.password_hash import HashPassword
from settings import get_db
from users.models import UserModel, UserLogsModel
from users.schemas import CreateUserRequest, LastVisitResponse


class UserCRUDService:
    def __init__(
        self,
        db: Session = Depends(get_db),
        password_hash: HashPassword = Depends(HashPassword),
    ):
        self._db = db
        self._password_hash = password_hash

    def create_user(self, data: CreateUserRequest):
        hash_password = self._password_hash.get_password_hash(data.password)
        user_data = {"email": data.email, "password": hash_password}
        try:
            user_obj = UserModel(**user_data)
            self._db.add(user_obj)
            self._db.commit()
        except Exception as e:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST, detail=USER_ALREADY_EXISTS
            )
        return MessageResponse(**{"message": REGISTRATION_SUCCESS})

    def last_activity(self, token: TokenData):
        last_visit = (
            self._db.query(UserLogsModel)
            .filter(UserLogsModel.user_id == token.user_id)
            .first()
        )
        if not last_visit:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, detail=DATA_NOT_FOUND
            )
        data = {
            "last_login_at": str(last_visit.last_login_at),
            "last_request_at": str(last_visit.last_request_at),
            "request_url": last_visit.request_url,
        }
        return LastVisitResponse(**data)
