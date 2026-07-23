from fastapi import APIRouter

router = APIRouter(
    prefix="/analytics",
    tags=["Analytics"]
)

@router.get("/")
def get_analytics():
    return {
        "totalPosts": 120,
        "scheduledPosts": 35,
        "publishedPosts": 85,
        "engagement": 78,
        "reach": 15420,
        "followers": 5200,
        "platformWise": {
            "Instagram": 2500,
            "Facebook": 1700,
            "LinkedIn": 1000
        },
        "chartData": [
            {"month": "Jan", "posts": 10},
            {"month": "Feb", "posts": 15},
            {"month": "Mar", "posts": 20},
            {"month": "Apr", "posts": 18}
        ]
    }