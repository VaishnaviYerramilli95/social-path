# SocialPilot – Social Media Scheduler & Campaign Management Platform

SocialPilot is a centralized social media scheduling and campaign management dashboard designed for content creators, startups, agencies, and social media managers. It enables users to connect social profiles, schedule media posts, bundle operations into marketing campaigns, inspect performance analytics, and export engagement reports.

---

## 💻 Tech Stack & Architecture

### Frontend
- **React.js**: Modern component-based view rendering.
- **Tailwind CSS**: Premium, responsive glassmorphic SaaS interface design.
- **Axios**: Promised-based API requests with automatic JWT token attachment.
- **Recharts**: Responsive chart animations for analytics graphs.

### Backend
- **FastAPI**: Scalable, high-performance async Python backend framework.
- **SQLAlchemy**: Object-Relational Mapper (ORM) to handle queries.
- **SQLite / PostgreSQL**: File-backed relational database storage.
- **python-jose (JWT) & bcrypt**: Encrypted password hashing and JWT state verification.

```text
React Frontend (Vite)
      ↓ (Axios HTTP Requests + JWT Authorization Bearer Token)
FastAPI REST API
      ↓ (Verify Token Dependency / Password hashing)
SQLAlchemy ORM
      ↓ (Queries)
SQLite Database (socialpilot.db)
```

---

## 📂 Project Directory Structure

```text
social-path/
├── docs/                           # Project technical documentation
│   ├── ARCHITECTURE.md
│   ├── TECH_STACK.md
│   ├── DATABASE.md
│   ├── API.md
│   ├── SETUP.md
│   ├── DEPLOYMENT.md
│   ├── USER_GUIDE.md
│   ├── PROJECT_WORKFLOW.md
│   ├── TESTING.md
│   └── PRESENTATION_GUIDE.md
├── frontend code/                  # Consolidated application workspace
│   ├── backend/                    # FastAPI python app
│   │   ├── app/
│   │   │   ├── models/             # SQLAlchemy DB schemas
│   │   │   ├── routers/            # API endpoint routes
│   │   │   ├── utils/              # Security and Seeding helpers
│   │   │   └── main.py             # Server initialization entrypoint
│   │   ├── requirements.txt        # Backend dependencies
│   │   └── socialpilot.db          # Persisted SQLite database
│   ├── frontend/                   # React Vite project
│   │   ├── src/
│   │   │   ├── components/         # Reusable cards, headers, layouts
│   │   │   ├── context/            # Auth and Theme provider states
│   │   │   ├── pages/              # Scheduler, Campaigns, Analytics, Settings
│   │   │   ├── services/           # Axios service methods
│   │   │   └── App.jsx             # React entry wrapper
│   │   ├── package.json            # React build dependencies
│   │   └── .env.development        # Configured backend API URL
│   ├── package.json                # Concurrently orchestration scripts
│   └── start-dev.ps1               # One-click Windows PowerShell scaffolding script
└── README.md                       # Main instruction file
```

---

## ⚡ Setup & Launch Instructions (Local Development)

### Automated Launch (Windows PowerShell)
Navigate to the consolidated directory and run the helper starter script:
```powershell
cd "frontend code"
./start-dev.ps1
```
*This will automatically scaffold the python virtual environment, install requirements, download NPM dependencies, build resources, and run both frontend and backend development servers concurrently.*

### Manual Cross-Platform Launch (macOS, Linux, CMD)

#### 1. Setup Backend:
```bash
cd "frontend code/backend"
python -m venv venv

# Activate venv
source venv/bin/activate  # On Linux/macOS
# OR
venv\Scripts\activate.bat # On Windows CMD

pip install -r requirements.txt
python -m uvicorn app.main:app --reload --host 127.0.0.1 --port 8000
```

#### 2. Setup Frontend:
```bash
cd "frontend code/frontend"
npm install
npm run dev
```
- **React Portal**: Access at `http://localhost:3000`
- **FastAPI OpenAPI Swagger**: Access at `http://localhost:8000/docs`

---

## 🔑 Environment Configuration

Create a `.env` file in `frontend code/backend/` following `.env.example`:
```ini
JWT_SECRET=your-secure-hash-secret-token-key
DATABASE_URL=sqlite:///./socialpilot.db
```

---

## 📝 Demo Seeding Mechanism

To make demonstrating the application's capabilities simple:
- Newly registered accounts are **automatically seeded** with realistic mockup campaigns, scheduled updates, connected profiles, alerts log, and historical chart datasets.
- Alternatively, triggering a `POST /auth/seed` request (with user token headers) regenerates the demonstration database instantly.

---

## 💡 Future Scope
1. **Real OAuth Integrations**: Connect directly to Facebook Graph API, Instagram Basic Display API, and Twitter/X Developer stream.
2. **Background Workers**: Integrate Redis and Celery task queues for scheduled time publishing triggers.
3. **AI Caption generation**: Integrate LLM suggestions for calendar media caption writes.
