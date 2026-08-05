import uuid
from sqlalchemy.orm import Session

from app.models.models import SocialAccount, Campaign, User
from app.schemas import SocialAccountCreate, SocialAccountUpdate, CampaignCreate, CampaignUpdate


# -------------------------
# Social Account CRUD
# -------------------------

def create_social_account(db: Session, account: SocialAccountCreate, user_id):
    db_account = SocialAccount(
        user_id=user_id,
        platform=account.platform,
        account_name=account.account_name,
        account_id=account.account_id,
        account_type=account.account_type,
        connection_status=account.connection_status,
        access_token=account.access_token,
        refresh_token=account.refresh_token,
        token_expiry=account.token_expiry,
        permissions=account.permissions,
        workspace=account.workspace,
        last_sync_time=account.last_sync_time,
    )

    db.add(db_account)
    db.commit()
    db.refresh(db_account)
    return db_account


def get_social_accounts(db: Session):
    return db.query(SocialAccount).all()


def get_social_account(db: Session, account_id):
    print("Received ID:", account_id)

    account = db.query(SocialAccount).filter(
        SocialAccount.id == account_id
    ).first()

    print("Result:", account)
    return account

def update_social_account(db: Session, account_id, account: SocialAccountUpdate):
    try:
        print("Received ID:", account_id)

        db_account = db.query(SocialAccount).filter(
            SocialAccount.id == account_id
        ).first()

        print("DB Account:", db_account)

        if not db_account:
            return None

        db_account.platform = account.platform
        db_account.account_name = account.account_name
        db_account.account_id = account.account_id
        db_account.account_type = account.account_type
        db_account.connection_status = account.connection_status
        db_account.access_token = account.access_token
        db_account.refresh_token = account.refresh_token
        db_account.token_expiry = account.token_expiry
        db_account.permissions = account.permissions
        db_account.workspace = account.workspace
        db_account.last_sync_time = account.last_sync_time

        db.commit()
        db.refresh(db_account)

        print("Updated Successfully")
        return db_account

    except Exception as e:
        print("ERROR:", e)
        raise


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
        status=campaign.status,
    )
    db.add(db_campaign)
    db.commit()
    db.refresh(db_campaign)
    return db_campaign


def get_campaigns(db: Session):
    return db.query(Campaign).all()

def get_campaign(db: Session, campaign_id: str):
    return db.query(Campaign).filter(Campaign.id == campaign_id).first()
    


def update_campaign(db: Session, campaign_id: str, campaign: CampaignUpdate):
    db_campaign = db.query(Campaign).filter(
        Campaign.id == campaign_id
    ).first()

    if not db_campaign:
        return None

    db_campaign.name = campaign.name
    db_campaign.platform = campaign.platform
    db_campaign.start_date = campaign.start_date
    db_campaign.end_date = campaign.end_date
    db_campaign.budget = campaign.budget
    db_campaign.objective = campaign.objective
    db_campaign.performance = campaign.performance
    db_campaign.status = campaign.status

    db.commit()
    db.refresh(db_campaign)
    return db_campaign


def delete_campaign(db: Session, campaign_id: str):
    campaign = db.query(Campaign).filter(
        Campaign.id == campaign_id
    ).first()

    if campaign:
        db.delete(campaign)
        db.commit()

    return campaign

    # ----------------------------
# User CRUD
# ----------------------------

def get_users(db: Session):
    return db.query(User).all()


def get_user(db: Session, user_id: str):
    return db.query(User).filter(User.id == user_id).first()


def update_user(db: Session, user_id: str, data: dict):
    user = db.query(User).filter(User.id == user_id).first()

    if not user:
        return None

    for key, value in data.items():
        setattr(user, key, value)

    db.commit()
    db.refresh(user)
    return user
def create_user(db: Session, user: User):
    db.add(user)
    db.commit()
    db.refresh(user)
    return user