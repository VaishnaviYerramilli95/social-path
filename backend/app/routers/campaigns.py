from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import get_db
from app import crud, schemas

router = APIRouter(
    prefix="/campaigns",
    tags=["Campaigns"]
)


@router.post("/", response_model=schemas.CampaignResponse)
def create_campaign(campaign: schemas.CampaignCreate, db: Session = Depends(get_db)):
    return crud.create_campaign(db, campaign)


@router.get("/", response_model=list[schemas.CampaignResponse])
def get_campaigns(db: Session = Depends(get_db)):
    return crud.get_campaigns(db)


@router.get("/{campaign_id}", response_model=schemas.CampaignResponse)
def get_campaign(campaign_id: str, db: Session = Depends(get_db)):
    campaign = crud.get_campaign(db, campaign_id)
    if not campaign:
        raise HTTPException(status_code=404, detail="Campaign not found")
    return campaign


@router.delete("/{campaign_id}")
def delete_campaign(campaign_id: str, db: Session = Depends(get_db)):
    campaign = crud.delete_campaign(db, campaign_id)
    if not campaign:
        raise HTTPException(status_code=404, detail="Campaign not found")
    return {"message": "Campaign deleted successfully"}