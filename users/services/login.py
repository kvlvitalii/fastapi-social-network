from fastapi import Depends, HTTPException, status
from sqlalchemy.orm import Session

from common.default_message import INVALID_DATA
from common.models import generate_current_datetime
from common.schemas import LoginResponse
from common.service.password_hash import HashPassword
from common.service.token import create_access_token
from settings import get_db
from users.models import UserModel, UserLogsModel
from users.schemas import LoginUser


class LoginService:
    def __init__(
        self,
        db: Session = Depends(get_db),
        password_hash: HashPassword = Depends(HashPassword),
    ):
        self._db = db
        self._password_hash = password_hash

    def login(self, data: LoginUser, url):
        user_obj = self._db.query(UserModel).filter(UserModel.email == data.email).first()
        if not user_obj:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"User with email: {data.email} not found.",
            )
        if not self._password_hash.verify_password(data.password, user_obj.password):
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST, detail=f"Invalid password!"
            )
        token = create_access_token(
            data={"email": user_obj.email, "user_id": str(user_obj.id)},
        )
        self._user_activity_logs(str(user_obj.id), str(url))
        return LoginResponse(**{"message": "Welcome!", "token": token})

    def _user_activity_logs(self, user_id, url):
        user_log = (
            self._db.query(UserLogsModel).filter(UserLogsModel.user_id == user_id).first()
        )
        user_log_data = {
            "user_id": user_id,
            "request_url": url,
            "login": generate_current_datetime(),
        }
        try:
            if not user_log:
                user_log_obj = UserLogsModel(**user_log_data)
                self._db.add(user_log_obj)
            else:
                user_log.request_url = url
                user_log.login = generate_current_datetime()
                user_log.updated_at = generate_current_datetime()
            self._db.commit()
        except Exception:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST, detail=INVALID_DATA
            )
