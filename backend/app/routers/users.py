from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import get_db
from app import crud

router = APIRouter(
    prefix="/users",
    tags=["Users"]
)

@router.get("/")
def get_users(db: Session = Depends(get_db)):
    return crud.get_users(db)

@router.put("/{user_id}")
def update_user(user_id: str, data: dict, db: Session = Depends(get_db)):
    user = crud.update_user(db, user_id, data)

    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    return user