from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.models import Campaign
from app.routers.scheduler import schedules
from app.routers.notifications import notifications
from app.utils.security import verify_token

router = APIRouter(
    prefix="/search",
    tags=["Search"]
)

@router.get("/")
def search(
    q: str = "",
    db: Session = Depends(get_db),
    user_id: str = Depends(verify_token)
):
    query_str = f"%{q}%"
    
    # 1. Search campaigns in database
    db_campaigns = db.query(Campaign).filter(
        Campaign.name.ilike(query_str) | 
        Campaign.objective.ilike(query_str) |
        Campaign.platform.ilike(query_str)
    ).all()
    
    # 2. Search schedules from memory
    matching_schedules = []
    if q:
        q_lower = q.lower()
        matching_schedules = [
            s for s in schedules
            if q_lower in s.get("content", "").lower() or q_lower in s.get("platform", "").lower()
        ]
        
    # 3. Search notifications from memory
    matching_notifications = []
    if q:
        q_lower = q.lower()
        matching_notifications = [
            n for n in notifications
            if q_lower in n.get("title", "").lower() or q_lower in n.get("message", "").lower()
        ]
        
    return {
        "campaigns": [
            {
                "id": c.id,
                "name": c.name,
                "platform": c.platform,
                "objective": c.objective,
                "status": c.status
            } for c in db_campaigns
        ],
        "schedules": matching_schedules,
        "notifications": matching_notifications
    }
