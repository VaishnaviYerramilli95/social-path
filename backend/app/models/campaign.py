import datetime
import uuid
from sqlalchemy import Column, String, Date, DateTime, ForeignKey, Text, Numeric
from sqlalchemy.dialects.postgresql import UUID
class Campaign:
    __tablename__ = "campaigns"
    id = Column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4,
        index=True
    )
    user_id = Column(
        UUID(as_uuid=True),
        ForeignKey("users.id"),
        nullable=False
    )
    name = Column(String, nullable=False)
    description = Column(Text, nullable=True)
    platform = Column(String, nullable=False)
    start_date = Column(Date, nullable=False)
    end_date = Column(Date, nullable=False)
    budget = Column(Numeric(10, 2), nullable=True)
    objective = Column(Text, nullable=True)
    status = Column(String, default="Upcoming")
    created_at = Column(
        DateTime,
        default=datetime.datetime.utcnow
    )
    updated_at = Column(
        DateTime,
        default=datetime.datetime.utcnow,
        onupdate=datetime.datetime.utcnow
    )