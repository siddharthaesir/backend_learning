# to run the application - uvicorn app.main:app --reload from root directory (E:\Projects\backend_engineering)
# http://127.0.0.1:8000/docs#/default/get_user_users__user_id__get

from fastapi import FastAPI
from app.routes import user

app = FastAPI()

app.include_router(user.router)
@app.get("/")
def home():
    return {"message":"Backend is running."}