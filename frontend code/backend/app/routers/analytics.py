from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.models import SocialAccount, Campaign
from app.utils.security import verify_token

router = APIRouter(
    prefix="/analytics",
    tags=["Analytics"]
)

@router.get("/")
def get_analytics(
    user_id: str = Depends(verify_token),
    db: Session = Depends(get_db)
):
    accounts = db.query(SocialAccount).filter(SocialAccount.user_id == user_id).all()

    platform_followers = {
        "Instagram": sum(acc.followers for acc in accounts if "instagram" in acc.platform.lower()),
        "Facebook": sum(acc.followers for acc in accounts if "facebook" in acc.platform.lower()),
        "LinkedIn": sum(acc.followers for acc in accounts if "linkedin" in acc.platform.lower()),
        "Twitter": sum(acc.followers for acc in accounts if "twitter" in acc.platform.lower())
    }

    total_followers = sum(platform_followers.values())
    reach = sum(acc.reach for acc in accounts)
    engagement = sum(acc.engagement for acc in accounts)
    clicks = int(reach * 0.04)

    overall_summary = {
        "totalEngagement": {"value": str(engagement), "change": "+12.4%", "trend": "up"},
        "totalFollowers": {"value": str(total_followers), "change": "+8.2%", "trend": "up"},
        "totalReach": {"value": str(reach), "change": "+15.3%", "trend": "up"},
        "totalClicks": {"value": str(clicks), "change": "+5.1%", "trend": "up"},
        "roi": {"value": "348%", "change": "+24.0%", "trend": "up"}
    }

    return {
        "overallSummary": overall_summary,
        "monthlyGrowth": [],
        "engagementTimeline": [],
        "platformComparison": [],
        "engagementRates": []
    }
