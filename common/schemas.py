from typing import Optional
from pydantic import BaseModel


class MessageResponse(BaseModel):
    message: str


class LoginResponse(MessageResponse):
    token: str


class TokenData(BaseModel):
    email: Optional[str] = None
    user_id: Optional[str] = None
