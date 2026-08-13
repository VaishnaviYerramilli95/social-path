# System Architecture Documentation

This document describes the design architecture, directory layout, and communication protocols of **SocialPilot**.

---

## 🏗️ Core Architecture Components

SocialPilot is structured as a decoupled full-stack SaaS platform containing:

1. **Client Layer (Frontend SPA)**: 
   - A single-page React app serving as the visual interface.
   - Built using Vite, React Router, Tailwind CSS, and Recharts.
   - Powered by Axios client instances that handle HTTP requests.
2. **Gateway / Security Layer (JWT Bearer Auth)**:
   - FastAPI middleware checks for incoming request headers.
   - Validates access tokens using cryptographic signatures (`jose`).
3. **Application Server (Backend API)**:
   - FastAPI server containing specific routers that manage modular business functions.
4. **Data Access / Persistence Layer**:
   - SQLAlchemy ORM engine mapping object models to relational SQLite/PostgreSQL tables.

```text
+---------------------------------------------------------+
|                  React Client Application               |
+---------------------------------------------------------+
                            │
                            │ Axios API requests
                            │ with JWT Bearer Token
                            ▼
+---------------------------------------------------------+
|                  FastAPI Endpoint Routers               |
|  (auth.py, scheduler.py, campaigns.py, analytics.py)   |
+---------------------------------------------------------+
                            │
                            │ Depends(verify_token)
                            ▼
+---------------------------------------------------------+
|               JWT Validation & Security                 |
+---------------------------------------------------------+
                            │
                            │ SQLAlchemy ORM queries
                            ▼
+---------------------------------------------------------+
|                    Relational Database                  |
|                 (socialpilot.db SQLite)                 |
+---------------------------------------------------------+
```

---

## 🔁 Key Workflows & Request Flows

### 1. Registration & Auto-Seeding Flow
```text
User Input (RegisterForm)
  │
  ▼
POST /auth/register
  │
  ├─► Password hashed (bcrypt)
  ├─► User record saved in DB
  ├─► seed_user_data() runs:
  │     ├── Inserts 4 connected Social Accounts
  │     ├── Inserts 4 default Campaigns
  │     ├── Inserts 6 Scheduled/Published/Failed Posts
  │     └── Inserts Analytics stats for past posts
  ▼
JSON Response (Access Token + Mapped User info)
```

### 2. Post Scheduling & Dashboard Analytics Flow
When a user schedules a post, the scheduler stores it under a `'scheduled'` status.
```text
React Scheduler UI ──► POST /scheduler/ ──► DB Table (Post)
                                              │
Dashboard UI ◄── GET /dashboard/ ◄────────────┤
                                              │
Analytics UI ◄── GET /analytics/ ◄────────────┘
  (Aggregates reach, likes, clicks dynamically)
```

---

## 🔒 Session Isolation & Multi-Tenancy

Every API endpoint managing business objects enforces user-ownership validation:
1. Every campaign, social channel link, notification, and scheduled post is stamped with a `user_id` FK.
2. Routers pull the authenticated user's ID using `current_user_id = Depends(verify_token)`.
3. All SELECT, UPDATE, and DELETE operations filter on the composite key `(id, user_id)`. Users cannot modify other profiles or view campaigns owned by other tokens.
