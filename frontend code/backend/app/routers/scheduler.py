from fastapi import APIRouter, HTTPException
import uuid

router = APIRouter(
    prefix="/scheduler",
    tags=["Scheduler"]
)

schedules = [
    {
        "id": "1",
        "campaign_id": "camp001",
        "platform": "Instagram",
        "content": "New product launch",
        "scheduled_time": "2026-07-23T18:00:00",
        "status": "scheduled"
    }
]

@router.get("/")
def get_scheduler():
    return schedules

@router.post("/")
def create_schedule(schedule: dict):
    schedule["id"] = str(uuid.uuid4())
    schedules.append(schedule)
    return schedule

@router.put("/{schedule_id}")
def update_schedule(schedule_id: str, data: dict):
    for schedule in schedules:
        if schedule["id"] == schedule_id:
            schedule.update(data)
            return schedule
    raise HTTPException(status_code=404, detail="Schedule not found")

@router.delete("/{schedule_id}")
def delete_schedule(schedule_id: str):
    for schedule in schedules:
        if schedule["id"] == schedule_id:
            schedules.remove(schedule)
            return {"message": "Schedule deleted"}
    raise HTTPException(status_code=404, detail="Schedule not found")