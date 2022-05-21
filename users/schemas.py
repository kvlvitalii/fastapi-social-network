from pydantic import BaseModel, EmailStr


class CreateUserRequest(BaseModel):
    email: EmailStr
    password: str


class LoginUser(BaseModel):
    email: str
    password: str


class LastVisitResponse(BaseModel):
    login: str
    updated_at: str
    request_url: str
