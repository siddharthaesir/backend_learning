# to run the application - uvicorn app.main:app --reload from root directory (E:\Projects\backend_engineering)

from fastapi import FastAPI
from app.routes import user

app = FastAPI()

app.include_router(user.router)
@app.get("/")
def home():
    return {"message":"Backend is running."}