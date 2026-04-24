from fastapi import APIRouter
from app.models.user import User

router = APIRouter()

@router.get("/users/{user_id}")
def get_user(user_id: int):
    print(f"Fetching User: {user_id}")
    return {
        "user_id": user_id,
        "name":"Test User"
    }
    
@router.post("/users")
def create_user(user: User):
    print(f"Creating user: {user}")
    return {
        "message":"User created",
        "user": user
    }