from datetime import datetime
from fastapi import HTTPException, status

from common.default_message import INVALID_DATA


def datatime_validator(data: str) -> datetime:
    try:
        data = datetime.strptime(data, "%Y-%m-%d")
        return data
    except Exception:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=INVALID_DATA)
