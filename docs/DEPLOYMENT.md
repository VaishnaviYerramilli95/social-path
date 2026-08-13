# Production Deployment Guide

This document describes how to deploy **SocialPilot** to production hosting platforms.

---

## 🌎 Recommended Deployment Architecture

- **Frontend**: Host on **Vercel** or **Netlify** (optimized for React SPA deployments).
- **Backend API**: Host on **Render**, **Railway**, or **Heroku** (FastAPI service container).
- **Production Database**: Deploy a managed **PostgreSQL** instance on **Supabase** or **Neon**.

---

## 🔒 Environment Variable Settings

### Backend Environments (FastAPI Server)
Inject these values in the platform configurations:
```ini
JWT_SECRET=your-secure-production-signature-key
DATABASE_URL=postgresql://user:password@host:5432/dbname
```

### Frontend Environments (React Client)
Deploy with:
```ini
VITE_API_BASE_URL=https://your-backend-api-domain.com
```

---

## 🌐 Configuring CORS (Cross-Origin Resource Sharing)

In production, the backend server must be configured to permit requests from the production frontend domain instead of `localhost:3000`.

Update `allow_origins` inside [main.py](file:///c:/Users/vaish/OneDrive/Desktop/social-path/frontend%20code/backend/app/main.py):
```python
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "https://your-frontend-domain.vercel.app",
        "http://localhost:3000"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
```

---

## 🚀 SQLite to PostgreSQL Database Migration

SQLAlchemy abstracts database queries. To switch from SQLite to PostgreSQL in production, simply update the `DATABASE_URL` environment variable to a valid PostgreSQL connection string. The engine will initialize all tables automatically using `Base.metadata.create_all(bind=engine)`.
