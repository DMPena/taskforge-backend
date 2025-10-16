from fastapi import FastAPI
from app.routers import task_router

app = FastAPI(title="TaskForge API")

# Register the task router
app.include_router(task_router.router)

@app.get("/")
def root():
    return {"message": "Welcome to TaskForge API!"}
