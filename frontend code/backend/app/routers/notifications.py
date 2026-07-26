from fastapi import APIRouter, HTTPException

router = APIRouter(
    prefix="/notifications",
    tags=["Notifications"]
)

notifications = [
    {
        "id": "1",
        "title": "Campaign Created",
        "message": "Campaign created successfully",
        "timestamp": "2026-07-23T10:00:00",
        "type": "success",
        "read": False
    },
    {
        "id": "2",
        "title": "Post Scheduled",
        "message": "Your post has been scheduled",
        "timestamp": "2026-07-23T11:00:00",
        "type": "info",
        "read": False
    }
]

@router.get("/")
def get_notifications():
    return notifications

@router.put("/read-all")
def mark_all_as_read():
    for notification in notifications:
        notification["read"] = True
    return {"success": True}


@router.put("/{notification_id}/read")
def mark_notification_as_read(notification_id: str):
    for notification in notifications:
        if notification["id"] == notification_id:
            notification["read"] = True
            return {"success": True}
    raise HTTPException(status_code=404, detail="Notification not found")


@router.delete("/")
def clear_notifications():
    notifications.clear()
    return {"success": True}


@router.delete("/{notification_id}")
def delete_single_notification(notification_id: str):
    for notification in notifications:
        if notification["id"] == notification_id:
            notifications.remove(notification)
            return {"success": True}
    raise HTTPException(status_code=404, detail="Notification not found")