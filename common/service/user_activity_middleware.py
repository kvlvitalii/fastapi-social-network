from fastapi import Request

from users.services.logger_service import LoggerService


class UserActivityMiddleware:

    async def __call__(self, request: Request, call_next):
        token = request.headers.get('authorization', '')
        url = str(request.url)
        LoggerService(token, url).refresh_log()
        response = await call_next(request)

        return response

