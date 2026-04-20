from fastapi import FastAPI

app = FastAPI()
@app.get("/")
def home():
    return {"message":"Backend is running."}

@app.get("/users/{user_id}")
def get_user(user_id: int):
    return {
        "user_id": user_id,
        "name":"Test User"
    }