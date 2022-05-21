from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer

from common.service.token import verify_token


class AuthUser:
    oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/v1/login")

    def __call__(self, token=Depends(oauth2_scheme)):
        token_data = verify_token(token)
        if token_data.email:
            return token_data
        else:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail=f"Sorry but you don't have access.",
            )
