# fastapi-social-network

#### Prepare (python3 version >= 3.10)
```bash
python3 -m venv ./venv
. venv/bin/activate
pip3 install -r requirements.txt
cp .env-exampl ./.env 
#conect to database change env variables 
alembic upgrade head
python3 main.py
```

#### Run with Docker
```bash
cp .env-exampl ./.env 
docker-compose up --build
```

### Postman-collections
In docs you find collections for postman