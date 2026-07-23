from fastapi import APIRouter, HTTPException
from app.schemas import UserCreate, UserLogin
from fastapi import Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.models import User
from app import crud
import uuid

router = APIRouter(
    prefix="/auth",
    tags=["Authentication"]
)


@router.post("/register")
def register(user: UserCreate, db: Session = Depends(get_db)):
    new_user = User(
        id=str(uuid.uuid4()),
        username=user.username,
        email=user.email,
        password=user.password
    )

    crud.create_user(db, new_user)

    return {
        "message": "User registered successfully"
    }

@router.post("/login")
def login(data: UserLogin, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.email == data.email).first()

    if not user:
        raise HTTPException(status_code=401, detail="Invalid email or password")

    if user.password != data.password:
        raise HTTPException(status_code=401, detail="Invalid email or password")

    return {
        "message": "Login successful",
        "user": {
            "id": user.id,
            "username": user.username,
            "email": user.email
        }
    }