from fastapi import FastAPI
from  app.database import engine, Base
from app.routers.social_accounts import router as social_router

app = FastAPI(
    title="SocialPilot API",
    version="1.0.0"
)

# Create all tables
Base.metadata.create_all(bind=engine)

# Register Social Account Router
app.include_router(social_router)


@app.get("/")
def home():
    return {
        "message": "Welcome to SocialPilot Backend"
    }