from fastapi.security import OAuth2PasswordRequestForm
from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.models import User
from app.schemas import UserCreate, UserLogin, SocialAccountCreate
from app import crud
from app.utils.security import (
    hash_password,
    verify_password,
    create_access_token
)
import uuid
from fastapi.responses import RedirectResponse
import requests

from app.config import (
    FACEBOOK_APP_ID,
    FACEBOOK_APP_SECRET,
    FACEBOOK_REDIRECT_URI,
)

router = APIRouter(
    prefix="/auth",
    tags=["Authentication"]
)


@router.post("/register")
def register(user: UserCreate, db: Session = Depends(get_db)):
    existing_user = db.query(User).filter(User.email == user.email).first()

    if existing_user:
        raise HTTPException(status_code=400, detail="Email already registered")

    new_user = User(
        id=str(uuid.uuid4()),
        username=user.username,
        email=user.email,
        password=hash_password(user.password)
    )

    crud.create_user(db, new_user)

    return {
        "message": "User registered successfully"
    }

    
@router.post("/login")
def login(
    form_data: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(get_db)
):
    user = db.query(User).filter(User.email == form_data.username).first()

    if not user:
        raise HTTPException(status_code=401, detail="Invalid email or password")

    if not verify_password(form_data.password, user.password):
        raise HTTPException(status_code=401, detail="Invalid email or password")

    access_token = create_access_token({"sub": user.id})
    return {
        "access_token": access_token,
        "token_type": "bearer",
        "user": {
            "id": user.id,
            "username": user.username,
            "email": user.email
        }
    }
@router.get("/facebook/login")
def facebook_login():
    facebook_url = (
        f"https://www.facebook.com/v23.0/dialog/oauth"
        f"?client_id={FACEBOOK_APP_ID}"
        f"&redirect_uri={FACEBOOK_REDIRECT_URI}"
        f"&scope=email,public_profile"
    )

    return RedirectResponse(facebook_url)


@router.get("/facebook/callback")
def facebook_callback(code: str, db: Session = Depends(get_db)):
    token_url = "https://graph.facebook.com/v23.0/oauth/access_token"

    token_response = requests.get(
        token_url,
        params={
            "client_id": FACEBOOK_APP_ID,
            "client_secret": FACEBOOK_APP_SECRET,
            "redirect_uri": FACEBOOK_REDIRECT_URI,
            "code": code,
        },
    )

    token_data = token_response.json()

    access_token = token_data.get("access_token")

    user_response = requests.get(
        "https://graph.facebook.com/me",
        params={
            "fields": "id,name",
            "access_token": access_token,
        },
    )

    user_data = user_response.json()

    social_account = SocialAccountCreate(
    platform="Facebook",
    account_name=user_data.get("name"),
    account_id=user_data.get("id"),
    account_type="Facebook",
    connection_status="connected",
    permissions="public_profile",
    workspace="default",
    access_token=access_token,
    refresh_token="",
)

   # crud.create_social_account(
    #     db,
    #   social_account,
    #  "00000000-0000-0000-0000-000000000001"
    #)

    return {
        "message": "Facebook account connected successfully",
        "facebook_user": user_data,
        "access_token": access_token
    }