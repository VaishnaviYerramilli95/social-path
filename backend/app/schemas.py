from pydantic import BaseModel
from typing import Optional
from uuid import UUID
from datetime import datetime
from pydantic import BaseModel


# -------------------------
# Social Account Schemas
# -------------------------

class SocialAccountBase(BaseModel):
    platform: str
    account_name: str
    account_id: Optional[str] = None
    account_type: Optional[str] = None
    connection_status: Optional[str] = "connected"
    permissions: Optional[str] = None
    workspace: Optional[str] = None


class SocialAccountCreate(SocialAccountBase):
    access_token: Optional[str] = None
    refresh_token: Optional[str] = None
    token_expiry: Optional[datetime] = None
    last_sync_time: Optional[datetime] = None


class SocialAccountUpdate(BaseModel):
    platform: str
    account_name: str
    account_id: str
    account_type: str
    connection_status: str
    access_token: str
    refresh_token: str
    token_expiry: datetime
    permissions: str
    workspace: str
    last_sync_time: datetime


class SocialAccountResponse(SocialAccountBase):
    id: UUID
    user_id: str
    token_expiry: Optional[datetime] = None
    last_sync_time: Optional[datetime] = None
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