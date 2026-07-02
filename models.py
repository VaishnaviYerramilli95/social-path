from sqlalchemy import Column, Integer, String, DateTime, Text
import datetime

# Note: Base class will be unified later by Leader
class Post:
    __tablename__ = "posts"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, nullable=False) # Will link to Member 2's User ID
    campaign_id = Column(Integer, nullable=True) # Will link to Member 5's Campaign ID
    
    content_text = Column(Text, nullable=True)
    media_url = Column(String, nullable=True) # AWS S3 or Cloudinary storage links
    post_type = Column(String, default="text") # text, image, video, carousel, story, reel
    
    status = Column(String, default="Draft") # Draft, Scheduled, Published, Failed, Cancelled
    
    scheduled_at = Column(DateTime, nullable=True) # Exact time to publish
    created_at = Column(DateTime, default=datetime.datetime.utcnow)