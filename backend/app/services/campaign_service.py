from datetime import date
from typing import List
from uuid import UUID
import uuid

from fastapi import HTTPException, status

from app.schemas.campaign import CampaignCreate, CampaignUpdate


campaigns = []


def calculate_campaign_status(start_date: date, end_date: date) -> str:
    today = date.today()

    if today < start_date:
        return "Upcoming"

    if start_date <= today <= end_date:
        return "Active"

    return "Completed"


def create_campaign(campaign: CampaignCreate):
    if campaign.end_date < campaign.start_date:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="End date cannot be before start date"
        )

    campaign_data = campaign.model_dump()
    campaign_data["id"] = uuid.uuid4()
    campaign_data["status"] = calculate_campaign_status(
        campaign.start_date,
        campaign.end_date
    )

    campaigns.append(campaign_data)

    return campaign_data


def get_campaigns() -> List[dict]:
    return campaigns


def get_campaign(campaign_id: UUID):
    for campaign in campaigns:
        if campaign.get("id") == campaign_id:
            return campaign

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Campaign not found"
    )


def update_campaign(campaign_id: UUID, campaign_update: CampaignUpdate):
    campaign = get_campaign(campaign_id)

    update_data = campaign_update.model_dump(exclude_unset=True)

    campaign.update(update_data)

    if "start_date" in update_data or "end_date" in update_data:
        campaign["status"] = calculate_campaign_status(
            campaign["start_date"],
            campaign["end_date"]
        )

    return campaign


def delete_campaign(campaign_id: UUID):
    campaign = get_campaign(campaign_id)

    campaigns.remove(campaign)

    return {
        "message": "Campaign deleted successfully"
    }