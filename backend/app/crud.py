from sqlalchemy.orm import Session
from app.models.models import SocialAccount
from app.schemas import SocialAccountCreate


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