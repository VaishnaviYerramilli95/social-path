import uuid
from sqlalchemy.orm import Session

from app.models.models import SocialAccount, Campaign
from app.schemas import SocialAccountCreate, CampaignCreate


# -------------------------
# Social Account CRUD
# -------------------------

def create_social_account(db: Session, account: SocialAccountCreate, user_id):
    db_account = SocialAccount(
        user_id=user_id,
        platform=account.platform,
        account_name=account.account_name,
        account_id=account.account_id,
        access_token=account.access_token,
        refresh_token=account.refresh_token,
    )
    db.add(db_account)
    db.commit()
    db.refresh(db_account)
    return db_account


def get_social_accounts(db: Session):
    return db.query(SocialAccount).all()


def get_social_account(db: Session, account_id):
    return db.query(SocialAccount).filter(
        SocialAccount.id == account_id
    ).first()


def delete_social_account(db: Session, account_id):
    account = db.query(SocialAccount).filter(
        SocialAccount.id == account_id
    ).first()

    if account:
        db.delete(account)
        db.commit()

    return account


# -------------------------
# Campaign CRUD
# -------------------------

def create_campaign(db: Session, campaign: CampaignCreate):
    db_campaign = Campaign(
        id=str(uuid.uuid4()),
        name=campaign.name,
        platform=campaign.platform,
        start_date=campaign.start_date,
        end_date=campaign.end_date,
        budget=campaign.budget,
        objective=campaign.objective,
        performance=campaign.performance,
    )
    db.add(db_campaign)
    db.commit()
    db.refresh(db_campaign)
    return db_campaign


def get_campaigns(db: Session):
    return db.query(Campaign).all()


def get_campaign(db: Session, campaign_id: str):
    return db.query(Campaign).filter(
        Campaign.id == campaign_id
    ).first()


def delete_campaign(db: Session, campaign_id: str):
    campaign = db.query(Campaign).filter(
        Campaign.id == campaign_id
    ).first()

    if campaign:
        db.delete(campaign)
        db.commit()

    return campaign