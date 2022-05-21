from common.models import generate_current_datetime
from common.service.token import verify_token
from settings import SessionLocal
from users.models import UserLogsModel


class LoggerService:
    def __init__(
        self,
        toket: str,
        url: str,
    ):
        self._token = toket
        self._url = url

    def refresh_log(self):
        if self._token:
            token_data = verify_token(self._token.split(" ")[1])
            db = SessionLocal()
            user_log = (
                db.query(UserLogsModel)
                .filter(UserLogsModel.user_id == token_data.user_id)
                .first()
            )
            user_log.request_url = self._url
            user_log.login = generate_current_datetime()
            user_log.updated_at = generate_current_datetime()
            db.commit()
