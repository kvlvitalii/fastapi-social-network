from pydantic import BaseModel, EmailStr


class CreateUserRequest(BaseModel):
    email: EmailStr
    password: str


class LoginUser(BaseModel):
    email: EmailStr
    password: str


class LastVisitResponse(BaseModel):
    last_login_at: str
    last_request_at: str
    request_url: str
