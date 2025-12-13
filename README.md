# FastAPI Auth Service

![Python](https://img.shields.io/badge/Python-3.13%2B-blue)
![Framework](https://img.shields.io/badge/FastAPI-backend-009688)
![Auth](https://img.shields.io/badge/Auth-JWT%20%7C%20HTTP%20Bearer-orange)
![Database](https://img.shields.io/badge/Database-SQLite%20%28Postgres--ready%29-lightgrey)
![Status](https://img.shields.io/badge/Status-Active-success)
![Scope](https://img.shields.io/badge/Scope-LLM%20Infrastructure-black)

A lightweight, production-ready authentication microservice built with FastAPI, designed as a foundational component for scalable LLM applications and modern backend systems.

## Features
- User registration with hashed passwords (bcrypt)
- JWT-based login and authorization
- Protected '/auth/me' endpoint using HTTP Bearer
- SQLite database using SQLAlchemy ORM (easily swappable to PostgreSQL)
- Environment-based configuration using Pydantic Settings
- Auto-generated interactive API docs (Swagger)
- Designed for integration into RAG systems, multi-agent backends, and LLM orchestration pipelines

## Tech Stack
FastAPI - Python web framework  
SQLAlchemy 2.0 - ORM  
JWT (python-jose) - token generation and validation  
Pydantic v2 and pydantic-settings - configuration management  
Uvicorn - ASGI server  
Python 3.13+

## Project structure
app/
├── auth/
│ ├── jwt_handler.py
│ ├── utils.py
│ └── router.py
├── config.py
├── database.py
├── models.py
├── schemas.py
└── main.py

## Setup and Installation
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
SECRET_KEY=changeme  
ALGORITHM=HS256  
ACCESS_TOKEN_EXPIRE_MINUTES=60
```  
5. Run the application  
```
uvicorn app.main:app --reload
```  
API available at:  
- Docs: http://127.0.0.1:8000/docs  
-  Docs: http://127.0.0.1:8000/health

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