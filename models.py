import datetime
import uuid
from sqlalchemy import Column, String, DateTime, ForeignKey, Text
from sqlalchemy.dialects.postgresql import UUID
# Base definition will be imported once database session config is initialized by lead

class Post:
    __tablename__ = "posts"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, index=True)
    user_id = Column(UUID(as_uuid=True), ForeignKey("users.id"), nullable=False) # Member 2 (Auth) connection
    campaign_id = Column(UUID(as_uuid=True), ForeignKey("campaigns.id"), nullable=True) # Member 5 (Campaign) connection
    
    caption = Column(Text, nullable=True) # Changed from content_text to caption based on Lead's blueprint
    media_url = Column(String, nullable=True) # AWS S3 or Cloudinary storage links
    
    schedule_time = Column(DateTime, nullable=True) # Changed from scheduled_at to schedule_time based on Lead's blueprint
    status = Column(String, default="Draft") # Draft, Scheduled, Published, Failed
    
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.datetime.utcnow, onupdate=datetime.datetime.utcnow)