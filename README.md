# FastAPI Auth Service

![Python](https://img.shields.io/badge/Python-3.13%2B-blue)
![Framework](https://img.shields.io/badge/FastAPI-backend-009688)
![Auth](https://img.shields.io/badge/Auth-JWT%20%7C%20HTTP%20Bearer-orange)
![Database](https://img.shields.io/badge/Database-PostgreSQL-blue)
![Deployment](https://img.shields.io/badge/Deploy-Fly.io-purple)
![CI/CD](https://img.shields.io/badge/CI%2FCD-GitHub%20Actions-black)
![Status](https://img.shields.io/badge/Status-Production--Ready-success)
![Scope](https://img.shields.io/badge/Scope-LLM%20Infrastructure-black)

---

## Overview

**FastAPI Auth Service** is a lightweight, production-ready authentication microservice built with FastAPI and PostgreSQL.


## Features
- User registration with **bcrypt-hashed passwords**  
- JWT-based authentication (HTTP Bearer)  
- Protected user context endpoint (`/auth/me`)  
- PostgreSQL database with **SQLAlchemy 2.0**  
- Schema versioning via **Alembic migrations**  
- Environment-based configuration (Pydantic Settings)  
- Dockerized for production deployment  
- Deployed on **Fly.io**  
- CI/CD pipeline using **GitHub Actions**  
- Designed for future extension (refresh tokens, rate limiting, LLM auth flows)  


## Architecture Overview
Client  
│  
│ HTTP (JWT Bearer)  
▼  
FastAPI Auth Service  
│  
│ SQLAlchemy ORM  
▼  
PostgreSQL (Fly.io)  
- Stateless API  
- Database schema managed exclusively via Alembic  
- Secrets managed via environment variables  
- Deployment automated through CI/CD  


## Tech Stack
- **FastAPI** – ASGI web framework  
- **Python 3.13**  
- **SQLAlchemy 2.0** – ORM  
- **PostgreSQL** – production database  
- **Alembic** – schema migrations  
- **JWT (python-jose)** – authentication tokens  
- **Pydantic v2** – settings & validation  
- **Docker** – containerization  
- **Fly.io** – cloud deployment  
- **GitHub Actions** – CI/CD  

## Project structure
app/  
├── auth/  
│ ├── router.py # Auth endpoints  
│ ├── jwt_handler.py # JWT creation & validation  
│ └── utils.py # Password hashing utilities  
├── config.py # Environment-based settings  
├── database.py # SQLAlchemy engine & session  
├── models.py # ORM models  
├── schemas.py # Pydantic schemas  
└── main.py # Application entrypoint  
alembic/  
├── versions/ # Migration history  
├── env.py # Alembic runtime config  
└── script.py.mako  
fly.toml # Fly.io deployment config  

## Local Development
1. Clone the repository  
```
git clone https://github.com/fuchs-martin/fastapi-auth-service.git  
cd fastapi-auth-service
```  
2. Create and activate a virtual environment  
```
python -m venv venv  
source venv/bin/activate    # macOS / Linux  
# or  
venv\Scripts\activate   # Windows
```  
3. Install dependencies  
```
pip install -r requirements.txt
```  
4. Configure environment variables  
Copy the example file:  
```
cp .env.example .env
```  
Update the values:  
```
ENV=local  
SECRET_KEY=changeme  
ALGORITHM=HS256  
ACCESS_TOKEN_EXPIRE_MINUTES=60  
DATABASE_URL=postgresql+psycopg://user:password@localhost:5432/dbname
```  
5. Run database migrations  
```
alembic upgrade head
```  
6. Start application  
```
uvicorn app.main:app --reload
```  
API available at:  
- Docs: http://127.0.0.1:8000/docs  
-  Docs: http://127.0.0.1:8000/health

## Deployment
The service is deployed on Fly.io and automatically updated via GitHub Actions on push to the main branch.  

Live URL:  
```
https://fastapi-auth-starter.fly.dev
```  
Health check:  
```
GET /health
```  

## API Endpoints
**Health**  
```
GET /health
```  
Return basic app status.

**Register**  
```
POST /auth/register
```  
Request body:   
```
{
  "email": "user@example.com",
  "password": "mypassword123"
}
```  
Response:  
```
{
  "id": 1,
  "email": "user@example.com"
}
```  
**Login**  
```
POST /auth/login
```  
Request body:  
```
{
  "email": "user@example.com",
  "password": "mypassword123"
}
```  
Response:  
```
{
  "access_token": "<jwt-token>",
  "token_type": "bearer"
}
```  
**Get Current User (Protected)**  
```
GET /auth/me
Authorization: Bearer <jwt-token>
```  
Response:  
```
{
  "id": 1,
  "email": "user@example.com"
}
```

## License
MIT License