from fastapi import APIRouter

router = APIRouter(
    prefix="/scheduler",
    tags=["Scheduler"]
)

@router.get("/")
def get_scheduler():
    return {"message": "Scheduler API Working"}