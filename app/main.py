from fastapi import FastAPI

from app.auth.router import router as auth_router

app = FastAPI(title="FastAPI Auth Services")


@app.get("/health")
def health():
    return {"status": "ok"}


app.include_router(auth_router)
