from fastapi import FastAPI

from app.auth.router import router as auth_router
from app.database import Base, engine
from app import models

Base.metadata.create_all(bind=engine)

app = FastAPI(title="FastAPI Auth Services")

@app.get("/health")
def health():
    return {"status": "ok"}

app.include_router(auth_router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)