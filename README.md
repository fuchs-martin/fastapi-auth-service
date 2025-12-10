# FastAPI Auth Service

A lightweight, production-ready authentication microservice built with FastAPI, designed as a foundational component for scalable LLM applications and modern backend systems.

## Overview
- User registration with hashed passwords (bcrypt)
- JWT-based login and authorization
- Protected '/auth/me' endpoint using HTTP Bearer
- SQLite database using SQLAlchemy ORM (easily swappable to PostgreSQL)
- Environment-based configuration using Pydantic Settings
- Auto-generated interactive API docs (Swagger)
- Designed for integration into RAG systems, multi-agent backends, and LLM orchestration pipelines

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
Requset body:  
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