from datetime import date, datetime
from decimal import Decimal
from typing import Optional
from uuid import UUID

from pydantic import BaseModel, ConfigDict, Field, field_validator, model_validator


SUPPORTED_PLATFORMS = {
    "Facebook",
    "Instagram",
    "LinkedIn",
    "X",
    "YouTube",
    "Pinterest",
}


class CampaignBase(BaseModel):
    name: str = Field(min_length=3, max_length=100)
    description: Optional[str] = None
    platform: str
    start_date: date
    end_date: date
    budget: Optional[Decimal] = Field(default=None, ge=0)
    objective: Optional[str] = None

    @field_validator("platform")
    @classmethod
    def validate_platform(cls, value: str):
        if value not in SUPPORTED_PLATFORMS:
            raise ValueError(
                "Platform must be Facebook, Instagram, LinkedIn, X, "
                "YouTube, or Pinterest"
            )

        return value

    @model_validator(mode="after")
    def validate_campaign_dates(self):
        if self.end_date < self.start_date:
            raise ValueError(
                "End date cannot be before start date"
            )

        return self


class CampaignCreate(CampaignBase):
    user_id: UUID


class CampaignUpdate(BaseModel):
    name: Optional[str] = Field(default=None, min_length=3, max_length=100)
    description: Optional[str] = None
    platform: Optional[str] = None
    start_date: Optional[date] = None
    end_date: Optional[date] = None
    budget: Optional[Decimal] = Field(default=None, ge=0)
    objective: Optional[str] = None
    status: Optional[str] = None

    @field_validator("platform")
    @classmethod
    def validate_platform(cls, value: Optional[str]):
        if value is not None and value not in SUPPORTED_PLATFORMS:
            raise ValueError("Unsupported social media platform")

        return value


class CampaignResponse(CampaignBase):
    id: UUID
    user_id: UUID
    status: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)