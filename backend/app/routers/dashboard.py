from fastapi import APIRouter

router = APIRouter(
    prefix="/dashboard",
    tags=["Dashboard"]
)

@router.get("/")
def get_dashboard():
    return {
        "totalPosts": 25,
        "scheduled": 10,
        "published": 13,
        "failed": 2,
        "campaignCount": 8,
        "connectedAccounts": 4
    }