from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from uuid import UUID

from app.database import get_db
from app.schemas import SocialAccountCreate, SocialAccountUpdate
from app import crud

router = APIRouter(
    prefix="/social-accounts",
    tags=["Social Accounts"]
)


@router.post("/")
def create_account(
    account: SocialAccountCreate,
    db: Session = Depends(get_db)
):
    # Temporary user_id until authentication is added
    user_id = "00000000-0000-0000-0000-000000000001"
    return crud.create_social_account(db, account, user_id)


@router.get("/")
def get_accounts(db: Session = Depends(get_db)):
    print("GET route called")
    return crud.get_social_accounts(db)


@router.get("/{account_id}")
def get_account(account_id: UUID, db: Session = Depends(get_db)):
    return crud.get_social_account(db, account_id)


@router.put("/{account_id}")
def update_account(account_id: UUID, account: SocialAccountUpdate, db: Session = Depends(get_db)):
    print("PUT API CALLED")
    return crud.update_social_account(db, account_id, account)


@router.delete("/{account_id}")
def delete_account(account_id: UUID, db: Session = Depends(get_db)):
    return crud.delete_social_account(db, account_id)
