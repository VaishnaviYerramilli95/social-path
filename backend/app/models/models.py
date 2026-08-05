import datetime
import uuid

from sqlalchemy import Column, String, DateTime, Float, Text
from sqlalchemy.dialects.postgresql import UUID

from app.database import Base


class SocialAccount(Base):
    __tablename__ = "social_accounts"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, index=True)

    user_id = Column(String, nullable=False)

    platform = Column(String, nullable=False)

    account_name = Column(String, nullable=False)

    account_id = Column(String, nullable=True)

    account_type = Column(String, nullable=True)

    connection_status = Column(String, default="connected")

    access_token = Column(Text, nullable=True)

    refresh_token = Column(Text, nullable=True)

    token_expiry = Column(DateTime, nullable=True)

    permissions = Column(Text, nullable=True)

    workspace = Column(String, nullable=True)

    last_sync_time = Column(DateTime, nullable=True)

    created_at = Column(DateTime, default=datetime.datetime.utcnow)

    updated_at = Column(
        DateTime,
        default=datetime.datetime.utcnow,
        onupdate=datetime.datetime.utcnow,
    )


class User(Base):
    __tablename__ = "users"

    id = Column(String, primary_key=True, index=True)
    username = Column(String, unique=True, nullable=False)
    email = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)
    phone = Column(String, nullable=True)
    company_name= Column(String, nullable=True)
    avatar= Column(String, nullable=True)


class Campaign(Base):
    __tablename__ = "campaigns"

    id = Column(String, primary_key=True, index=True, default=lambda: str(uuid.uuid4()))
    name = Column(String, nullable=False)
    platform = Column(String, nullable=False)
    start_date = Column(String)
    end_date = Column(String)
    budget = Column(Float)
    objective = Column(String)
    performance = Column(String)
    status = Column(String)