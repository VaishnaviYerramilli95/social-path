from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.routes.campaign import router as campaign_router


app = FastAPI(
    title="SocialPilot API",
    description="Social Media Scheduler & Campaign Management Platform",
    version="1.0.0",
)


app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:3000",
        "http://localhost:5173",
        "http://127.0.0.1:3000",
        "http://127.0.0.1:5173",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(campaign_router)


@app.get("/")
def root():
    return {
        "message": "SocialPilot API is running"
    }