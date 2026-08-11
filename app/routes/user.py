from fastapi import APIRouter
from app.schemas.user import UserCreate
from sqlalchemy.orm import Session
from fastapi import Depends, HTTPException
from app.db import get_db
from app.models.user import User
from app.schemas.user import UserCreate, UserUpdate, UserResponse
from sqlalchemy.exc import IntegrityError


router = APIRouter()

#GET
@router.get("/users/{user_id}", response_model=UserResponse)
def get_user(user_id: int, db: Session = Depends(get_db)):
    
    # User.id is column metadata which SQLAlchemy.ORM converts in to SQL expression, user.id is actual row value, 
    # SQLAlechmy overloads "==" operator and creates SQL expression tree. This is a way to do Database absraction along with many other things. 
    user = db.query(User).filter(User.id == user_id).first()                

    if user is None:
         raise HTTPException(
              status_code=404,
              detail="User not found"
         )
    
    return user 

#PUT
@router.put("/users/{user_id}", response_model=UserResponse)
def update_user(
     user_id: int,
     updated_user: UserUpdate,
     db: Session = Depends(get_db)
):
     
     user = db.query(User).filter(User.id == user_id).first()

     if user is None:
          raise HTTPException(
               status_code=404,
               detail="User not found"
          )
     
     user.name = updated_user.name           # SQLAlchemy updating python object's detail, marking it dirty in the process until db commit. 
     user.email = updated_user.email         # this saves generating multitple SQLs, batches the changes, UPDATEs & COMMITs happen when db.commit() is run.
     user.phone = updated_user.phone         # This bunches updates as a "Unit of Work".
     
     try:
         db.commit()             #ORM will generate the UPDATE cmd, then commit to DB
         db.refresh(user)
     
     except IntegrityError:
          db.rollback()
     
          raise HTTPException(
               status_code=409,
               detail="Email already exists"
          )
     
     return user
     

#POST    

# "db: Session = Depends(get_db)" below injects dependency,
# FASTAPI: creates DB session, injects in into request, closes afterward

@router.post("/users", response_model=UserResponse)
def create_user(user: UserCreate, db: Session = Depends(get_db)):

# pydantic_schema_object -> SQLAlchemy_ORM_object conversion    
    db_user = User(
        id = user.id,
        name = user.name,
        email = user.email,
        phone = user.phone
    )

    try:
        # INSERT
            db.add(db_user)

        # COMMIT
            db.commit()

        # Reloadin object from DB, potential use = generating IDs, defaults, triggers
            db.refresh(db_user)


            return db_user

    except IntegrityError:
        db.rollback()

        raise HTTPException(
             status_code=409,
             detail="User with given ID or email already exists"
        )

@router.delete("/users/{user_id}")
def delete_user(
     user_id: int,
     db: Session = Depends(get_db)
):

     user = db.query(User).filter(User.id == user_id).first()
     if user is None:
          raise HTTPException(
               status_code=404,
               detail="User not found"
          )
     
     db.delete(user)
     db.commit()

     return{
          "message": f"User {user_id} deleted successfully"
     }