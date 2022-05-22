import os

import dotenv

dotenv.load_dotenv()

DB_HOST_US = os.getenv("DB_HOST_US")
DB_PORT_US = int(os.getenv("DB_PORT_US"))
DB_NAME_US = os.getenv("DB_NAME_US")
DB_USERNAME_US = os.getenv("DB_USERNAME_US")
DB_PASSWORD_US = os.getenv("DB_PASSWORD_US")
SECRET_KEY_JWT = os.getenv("SECRET_KEY_JWT")
ALGORITHM = os.getenv("ALGORITHM")
ACCESS_TOKEN_EXPIRE_MINUTES = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES"))
