from pydantic import BaseModel
from typing import Optional
from uuid import UUID
from datetime import datetime


# -------------------------
# Social Account Schemas
# -------------------------

class SocialAccountBase(BaseModel):
    platform: str
    account_name: str
    account_id: Optional[str] = None


class SocialAccountCreate(SocialAccountBase):
    access_token: Optional[str] = None
    refresh_token: Optional[str] = None


class SocialAccountResponse(SocialAccountBase):
    id: UUID
    user_id: str
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True


# -------------------------
# User Schemas
# -------------------------

class UserCreate(BaseModel):
    username: str
    email: str
    password: str
    phone: Optional[str] = None
    company_name: Optional[str] = None


class UserLogin(BaseModel):
    email: str
    password: str


class UserResponse(BaseModel):
    id: str
    username: str
    email: str
    phone: str | None = None
    company_name: str | None = None
    avatar: str | None = None

    class Config:
        from_attributes = True


class UserUpdate(BaseModel):
    username: str | None = None
    email: str | None = None
    phone: str | None = None
    company_name: str | None = None
    avatar: str | None = None

 # -------------------------
# Campaign Schemas
# -------------------------

class CampaignBase(BaseModel):
    name: str
    platform: str
    start_date: str
    end_date: str
    budget: float
    objective: str
    performance: str
    status: str

class CampaignCreate(CampaignBase):
    pass

class CampaignUpdate(CampaignBase):
    pass

class CampaignResponse(CampaignBase):
    id: str

    class Config:
        from_attributes = True


class PasswordChangeRequest(BaseModel):
    currentPassword: str
    newPassword: str 