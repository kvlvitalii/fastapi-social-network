from datetime import datetime, timedelta

from fastapi import HTTPException, status
from jose import JWTError, jwt

from common.schemas import TokenData
from config import ACCESS_TOKEN_EXPIRE_MINUTES, SECRET_KEY_JWT, ALGORITHM


def create_access_token(data: dict):
    expires_delta = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode = data.copy()
    expire = datetime.utcnow() + expires_delta
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY_JWT, algorithm=ALGORITHM)
    return encoded_jwt


def verify_token(
    token: str,
):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials.",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY_JWT, algorithms=[ALGORITHM])
        return TokenData(email=payload.get("email"), user_id=payload.get("user_id"))
    except JWTError:
        raise credentials_exception
