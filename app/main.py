from fastapi import FastAPI

from app.auth.router import router as auth_router
from app.database import Base, engine
from app import models

app = FastAPI(title="FastAPI Auth Services")

@app.on_event("startup")
def on_startup():
    Base.metadata.create_all(bind=engine)

@app.get("/health")
def health():
    return {"status": "ok"}

app.include_router(auth_router)
