from pydantic import BaseModel
from typing import Optional
from uuid import UUID
from datetime import datetime


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