from uuid import UUID

from fastapi import APIRouter

from app.schemas.campaign import CampaignCreate, CampaignUpdate
from app.services.campaign_service import (
    create_campaign,
    get_campaigns,
    get_campaign,
    update_campaign,
    delete_campaign,
)


router = APIRouter(
    prefix="/campaigns",
    tags=["Campaign Management"]
)


@router.post("/")
def create_new_campaign(campaign: CampaignCreate):
    return create_campaign(campaign)


@router.get("/")
def list_campaigns():
    return get_campaigns()


@router.get("/{campaign_id}")
def campaign_details(campaign_id: UUID):
    return get_campaign(campaign_id)


@router.put("/{campaign_id}")
def edit_campaign(
    campaign_id: UUID,
    campaign: CampaignUpdate
):
    return update_campaign(campaign_id, campaign)


@router.delete("/{campaign_id}")
def remove_campaign(campaign_id: UUID):
    return delete_campaign(campaign_id)