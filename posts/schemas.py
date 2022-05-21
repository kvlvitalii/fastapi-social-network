from pydantic import BaseModel


class PostRequest(BaseModel):
    header: str
    text: str


class PostCreateResponse(BaseModel):
    message: str
    post_id: str
