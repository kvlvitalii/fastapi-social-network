import uvicorn
import dotenv

from fastapi import FastAPI
from starlette.middleware.base import BaseHTTPMiddleware

from common.service.user_activity_middleware import UserActivityMiddleware
from posts.routes import post_router, like_router
from users.routes import user_router

dotenv.load_dotenv()

app = FastAPI(
    title="User Service API",
    docs_url="/docs",
)
my_middleware = UserActivityMiddleware()
app.add_middleware(BaseHTTPMiddleware, dispatch=my_middleware)


app.include_router(user_router)
app.include_router(post_router)
app.include_router(like_router)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", log_level="info")
