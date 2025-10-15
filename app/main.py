from fastapi import FastAPI
from app.routers import hello

app = FastAPI(title="TaskForge Backend")

app.include_router(hello.router)