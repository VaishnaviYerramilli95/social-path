# Project Technical Documentation: SocialPilot

**SocialPilot** is a full-stack, multi-tenant social media scheduling and campaign management dashboard designed for content creators, agencies, and social media managers. It provides a centralized hub to link mock social channels, group postings under marketing campaigns, verify content schedules on a visual calendar, inspect aggregated performance metrics, and export spreadsheet reports.

---

## 📄 1. Abstract
In the modern digital workspace, coordinating social media output across diverse channels is highly fragmented. Content managers must juggle multiple platform credentials, disconnected post queues, and isolated metrics dashboards. **SocialPilot** solves this by unifying campaigns, visual scheduling, analytics, and team collaboration into a single, cohesive dashboard.

The application leverages a decoupled client-server architecture. The frontend is built as a single-page application (SPA) using React.js and Tailwind CSS, utilizing Axios for API requests. The backend is a high-performance REST API built with FastAPI, utilizing SQLAlchemy ORM to manage state and relational queries. Data isolation is maintained via secure JWT tokens, ensuring that each authenticated user's workspace, social links, campaigns, and posts remain strictly private.

---

## ⚠️ 2. Problem Statement & Objectives
### The Problem
1. **Disconnected Channels**: Navigating different interfaces for Facebook, Instagram, LinkedIn, and Twitter/X is slow and inefficient.
2. **Disconnected Marketing Budgets**: Social media schedules are rarely tracked alongside financial budgets or target campaign objectives.
3. **Complex Performance Reporting**: Consolidating performance stats (likes, impressions, clicks, shares) across networks is labor-intensive.
4. **Data Privacy & Isolation**: Multi-tenant systems require a database design that guarantees agency workspaces cannot leak into another user's view.

### The Objectives
- **Centralized Console**: A responsive, modern interface to view connected accounts, campaigns, schedules, and analytics.
- **Relational Post Scheduling**: Link scheduled updates to specific active marketing campaigns to align content and budgets.
- **Stateless Authentication**: Implement JWT session management for user authentication and multi-tenant row isolation.
- **Demonstration Seeding Engine**: Automatically seed new accounts with realistic mockup campaigns, analytics histories, connected channels, and notifications for immediate demonstration.

---

## 📐 3. Comparison: Requirements vs. Implementation

Below is the authoritative compliance table mapping the official project requirements (PDF specifications) against the actual codebase in the repository.

| Requirement | Implemented? | Where Implemented | Evidence (Code References) | Status |
| :--- | :--- | :--- | :--- | :--- |
| **User Sign-up & Login** | **FULLY IMPLEMENTED** | Backend Routers & Frontend Pages | [auth.py](file:///c:/Users/vaish/OneDrive/Desktop/social-path/frontend%20code/backend/app/routers/auth.py), [Login.jsx](file:///c:/Users/vaish/OneDrive/Desktop/social-path/frontend%20code/frontend/src/pages/Login.jsx) | **GREEN = Working** |
| **Password Hashing** | **FULLY IMPLEMENTED** | Backend Security Utilities | [security.py](file:///c:/Users/vaish/OneDrive/Desktop/social-path/frontend%20code/backend/app/utils/security.py) (uses `passlib[bcrypt]`) | **GREEN = Working** |
| **Social Account Connect** | **DEMO / MOCK IMPLEMENTATION** | Frontend Connection Modal | [SocialAccounts.jsx](file:///c:/Users/vaish/OneDrive/Desktop/social-path/frontend%20code/frontend/src/pages/SocialAccounts.jsx) (simulated popup & mock tokens) | **YELLOW = Partial/Demo** |
| **Campaign Budget/Objective** | **FULLY IMPLEMENTED** | Campaigns CRUD Router & DB Models | [campaigns.py](file:///c:/Users/vaish/OneDrive/Desktop/social-path/frontend%20code/backend/app/routers/campaigns.py), [models.py](file:///c:/Users/vaish/OneDrive/Desktop/social-path/frontend%20code/backend/app/models/models.py#L53) | **GREEN = Working** |
| **Visual Calendar Scheduling** | **FULLY IMPLEMENTED** | Frontend Calendar UI & Backend Router | [Scheduler.jsx](file:///c:/Users/vaish/OneDrive/Desktop/social-path/frontend%20code/frontend/src/pages/Scheduler.jsx), [Calendar.jsx](file:///c:/Users/vaish/OneDrive/Desktop/social-path/frontend%20code/frontend/src/components/Calendar.jsx) | **GREEN = Working** |
| **Live Social Publishing** | **DEMO / MOCK IMPLEMENTATION** | Scheduler DB State Updates | [seeding.py](file:///c:/Users/vaish/OneDrive/Desktop/social-path/frontend%20code/backend/app/utils/seeding.py), [schedulerService.js](file:///c:/Users/vaish/OneDrive/Desktop/social-path/frontend%20code/frontend/src/services/schedulerService.js) | **YELLOW = Partial/Demo** |
| **Performance Analytics Charts** | **FULLY IMPLEMENTED** | Analytics API & Recharts | [analytics.py](file:///c:/Users/vaish/OneDrive/Desktop/social-path/frontend%20code/backend/app/routers/analytics.py), [Analytics.jsx](file:///c:/Users/vaish/OneDrive/Desktop/social-path/frontend%20code/frontend/src/pages/Analytics.jsx) | **GREEN = Working** |
| **Multi-Platform Reports** | **FULLY IMPLEMENTED** | Frontend Reports Service | [Reports.jsx](file:///c:/Users/vaish/OneDrive/Desktop/social-path/frontend%20code/frontend/src/pages/Reports.jsx) (platform filtering + CSV export) | **GREEN = Working** |
| **Notifications & System Alerts** | **FULLY IMPLEMENTED** | Notifications API & Bell Hub | [notifications.py](file:///c:/Users/vaish/OneDrive/Desktop/social-path/frontend%20code/backend/app/routers/notifications.py), [NotificationCard.jsx](file:///c:/Users/vaish/OneDrive/Desktop/social-path/frontend%20code/frontend/src/components/NotificationCard.jsx) | **GREEN = Working** |
| **Multi-Tenant User Isolation** | **FULLY IMPLEMENTED** | JWT dependencies on all routers | [crud.py](file:///c:/Users/vaish/OneDrive/Desktop/social-path/frontend%20code/backend/app/crud.py) (all selects filter by `user_id`) | **GREEN = Working** |
| **Notification Settings Save** | **NOT IMPLEMENTED** | Settings Tab Preferences | [Settings.jsx](file:///c:/Users/vaish/OneDrive/Desktop/social-path/frontend%20code/frontend/src/pages/Settings.jsx#L265) (state is local only, does not persist) | **RED = Missing/Broken** |

---

## 🏛️ 4. Complete Project Architecture & Request Flow

SocialPilot uses a modern client-server decoupled design. Below is the request and data flow of the application:

```text
React Frontend (Vite)
       │
       │ 1. User performs action (e.g., schedules post, creates campaign)
       │ 2. Frontend initiates Axios call
       │ 3. Request Interceptor attaches JWT token: Authorization: Bearer <token>
       ▼
FastAPI Gateway Router (Uvicorn Engine)
       │
       │ 4. Endpoint intercepts request
       │ 5. Checks dependency: user_id: str = Depends(verify_token)
       │ 6. Cryptographically decodes token; extracts sub (user_id)
       ▼
CRUD & Query Layer
       │
       │ 7. SQLAlchemy query constructor filters operations strictly by user_id
       │    e.g., db.query(Post).filter(Post.user_id == user_id).all()
       ▼
SQLAlchemy ORM Data Engine
       │
       │ 8. Compiles Python ORM declarations into dialect-specific SQL
       ▼
PostgreSQL (Supabase) / SQLite (Local)
       │
       │ 9. Relational queries execute safely on the database server
       │ 10. Mapped database rows are returned to the SQLAlchemy engine
       ▼
FastAPI Gateway Router
       │
       │ 11. Endpoint converts database models into JSON schemas (Pydantic models)
       │ 12. Sends HTTP response payload back to the client
       ▼
React Frontend
       │
       │ 13. State hook triggers re-render (e.g., setPosts(data))
       │ 14. Responsive Tailwind view updates instantly without page reload
```

### Technical Terminology for Viva
- **REST APIs**: Representational State Transfer. A client-server architectural style that communicates over standard HTTP protocols.
- **HTTP Methods**: Operations that specify actions on resource endpoints:
  - `GET`: Fetch data (e.g., retrieve campaign summaries).
  - `POST`: Create new data (e.g., schedule a post).
  - `PUT`: Edit/update existing database rows (e.g., modify user details).
  - `DELETE`: Remove records permanently (e.g., link disconnection).
- **JSON (JavaScript Object Notation)**: Text-based format utilized to transmit structured data objects between client and server.
- **CORS (Cross-Origin Resource Sharing)**: Security mechanism configured in [main.py](file:///c:/Users/vaish/OneDrive/Desktop/social-path/frontend%20code/backend/app/main.py#L37) to permit the React application (hosted on localhost:3000 or Vercel) to query endpoints on the FastAPI server (hosted on localhost:8000 or Render).
- **JWT (JSON Web Token)**: Stateless authentication standard using cryptographically signed tokens to store user identities (IDs), preventing the backend from needing stateful database session lookups.
- **User Isolation**: A relational database practice where every data mutation is restricted by checking the requester's `user_id` foreign key.

---

## 👥 5. Every Module Detailed Explanation

### 1. Authentication
- **Problem it Solves**: Prevents unauthorized API access and isolates multi-tenant workspaces.
- **User Actions**: Submits credentials on registration or login views.
- **Frontend Files**: [Login.jsx](file:///c:/Users/vaish/OneDrive/Desktop/social-path/frontend%20code/frontend/src/pages/Login.jsx), [Register.jsx](file:///c:/Users/vaish/OneDrive/Desktop/social-path/frontend%20code/frontend/src/pages/Register.jsx), [AuthContext.jsx](file:///c:/Users/vaish/OneDrive/Desktop/social-path/frontend%20code/frontend/src/context/AuthContext.jsx).
- **Backend Files**: [auth.py](file:///c:/Users/vaish/OneDrive/Desktop/social-path/frontend%20code/backend/app/routers/auth.py).
- **API Endpoints**: `POST /auth/register`, `POST /auth/login`, `POST /auth/seed`.
- **Database Tables**: `users`.
- **Important Logic**: Hashes passwords on registration using `passlib[bcrypt]`. Generates and returns a JWT token signed with `python-jose`.
- **Status**: **Fully database-backed**.
- **Demonstration**: Register a new user, log out, and log back in to show token validation.

### 2. User & Profile
- **Problem it Solves**: Manages user details (phone, company) and roles.
- **User Actions**: Updates details on the profile tab.
- **Frontend Files**: [Profile.jsx](file:///c:/Users/vaish/OneDrive/Desktop/social-path/frontend%20code/frontend/src/pages/Profile.jsx), [userService.js](file:///c:/Users/vaish/OneDrive/Desktop/social-path/frontend%20code/frontend/src/services/userService.js).
- **Backend Files**: [users.py](file:///c:/Users/vaish/OneDrive/Desktop/social-path/frontend%20code/backend/app/routers/users.py).
- **API Endpoints**: `GET /users/profile`, `PUT /users/{user_id}`, `POST /users/change-password`.
- **Database Tables**: `users`.
- **Status**: **Fully database-backed**.
- **Demonstration**: Edit the company name or phone number on the Profile page, save, and refresh to verify persistence.

### 3. Dashboard Overview
- **Problem it Solves**: Summarizes total posts, active campaigns, linked channels, and scheduling status counts.
- **User Actions**: View summary stats.
- **Frontend Files**: [Dashboard.jsx](file:///c:/Users/vaish/OneDrive/Desktop/social-path/frontend%20code/frontend/src/pages/Dashboard.jsx), [StatsCard.jsx](file:///c:/Users/vaish/OneDrive/Desktop/social-path/frontend%20code/frontend/src/components/StatsCard.jsx).
- **Backend Files**: [dashboard.py](file:///c:/Users/vaish/OneDrive/Desktop/social-path/frontend%20code/backend/app/routers/dashboard.py).
- **API Endpoints**: `GET /dashboard/`.
- **Database Tables**: `social_accounts`, `campaigns`, `posts`.
- **Important Logic**: Aggregates counts of posts grouped by status (`scheduled`, `published`, `failed`) and active campaigns.
- **Status**: **Fully database-backed**.
- **Demonstration**: Link a new social channel or create a campaign, and check the dashboard summary counts.

### 4. Social Accounts (OAuth)
- **Problem it Solves**: Links user profiles to publish content.
- **User Actions**: Click platform icons, enter a profile handle, and trigger mock authentication.
- **Frontend Files**: [SocialAccounts.jsx](file:///c:/Users/vaish/OneDrive/Desktop/social-path/frontend%20code/frontend/src/pages/SocialAccounts.jsx), [socialAccountService.js](file:///c:/Users/vaish/OneDrive/Desktop/social-path/frontend%20code/frontend/src/services/socialAccountService.js).
- **Backend Files**: [social_accounts.py](file:///c:/Users/vaish/OneDrive/Desktop/social-path/frontend%20code/backend/app/routers/social_accounts.py).
- **API Endpoints**: `GET /social-accounts/`, `POST /social-accounts/`, `DELETE /social-accounts/{id}`.
- **Database Tables**: `social_accounts`.
- **Important Logic**: Generates mock OAuth validation tokens (`mock_tok_...`) and saves account details to the database under the user's ID.
- **Status**: **Simulated OAuth (Mock) / Database-backed**.
- **Demonstration**: Open the Social Accounts page, click "Add Instagram Profile", enter `@brand_dev`, and link the account.

### 5. Campaigns
- **Problem it Solves**: Groups related content plans, manages budgets, objectives, and channels.
- **User Actions**: Create, edit, and delete campaigns.
- **Frontend Files**: [Campaigns.jsx](file:///c:/Users/vaish/OneDrive/Desktop/social-path/frontend%20code/frontend/src/pages/Campaigns.jsx), [CampaignCard.jsx](file:///c:/Users/vaish/OneDrive/Desktop/social-path/frontend%20code/frontend/src/components/CampaignCard.jsx), [campaignService.js](file:///c:/Users/vaish/OneDrive/Desktop/social-path/frontend%20code/frontend/src/services/campaignService.js).
- **Backend Files**: [campaigns.py](file:///c:/Users/vaish/OneDrive/Desktop/social-path/frontend%20code/backend/app/routers/campaigns.py).
- **API Endpoints**: `GET /campaigns/`, `POST /campaigns/`, `PUT /campaigns/{campaign_id}`, `DELETE /campaigns/{campaign_id}`.
- **Database Tables**: `campaigns`.
- **Status**: **Fully database-backed**.
- **Demonstration**: Create a campaign named "Product Launch v2", assign a budget, and verify that it appears on the dashboard.

### 6. Scheduler (Post Publishing)
- **Problem it Solves**: Provides a visual interface to plan and queue updates.
- **User Actions**: Double-click calendar dates, enter details, and schedule posts.
- **Frontend Files**: [Scheduler.jsx](file:///c:/Users/vaish/OneDrive/Desktop/social-path/frontend%20code/frontend/src/pages/Scheduler.jsx), [Calendar.jsx](file:///c:/Users/vaish/OneDrive/Desktop/social-path/frontend%20code/frontend/src/components/Calendar.jsx), [schedulerService.js](file:///c:/Users/vaish/OneDrive/Desktop/social-path/frontend%20code/frontend/src/services/schedulerService.js).
- **Backend Files**: [scheduler.py](file:///c:/Users/vaish/OneDrive/Desktop/social-path/frontend%20code/backend/app/routers/scheduler.py).
- **API Endpoints**: `GET /scheduler/`, `POST /scheduler/`, `PUT /scheduler/{post_id}`, `DELETE /scheduler/{post_id}`.
- **Database Tables**: `posts`, `campaigns`.
- **Important Logic**: Formats dates into `YYYY-MM-DDTHH:MM:00` strings. Mapped to campaign folders. Post publishing is **simulated** (posts are saved to the database; they do not post to real social APIs).
- **Status**: **Simulated Publishing / Database-backed**.
- **Demonstration**: Schedule a post on the visual calendar grid, and verify that it appears on the specified date.

### 7. Analytics Overview
- **Problem it Solves**: Displays total reach, followers, clicks, ROI, and weekly engagement timelines.
- **User Actions**: View performance statistics.
- **Frontend Files**: [Analytics.jsx](file:///c:/Users/vaish/OneDrive/Desktop/social-path/frontend%20code/frontend/src/pages/Analytics.jsx), [analyticsService.js](file:///c:/Users/vaish/OneDrive/Desktop/social-path/frontend%20code/frontend/src/services/analyticsService.js).
- **Backend Files**: [analytics.py](file:///c:/Users/vaish/OneDrive/Desktop/social-path/frontend%20code/backend/app/routers/analytics.py).
- **API Endpoints**: `GET /analytics/`.
- **Database Tables**: `analytics`, `posts`.
- **Important Logic**: Sums metrics (likes, shares, clicks) from the `analytics` table. Fallbacks are applied if a user has no published posts to populate the charts.
- **Status**: **Aggregated from Database with simulated fallbacks**.
- **Demonstration**: Show the Analytics page and point to the engagement timelines and ROI charts.

### 8. Reports
- **Problem it Solves**: Provides comparison logs and exports post data.
- **User Actions**: Apply platform filters and click "Post Logs" to download reports.
- **Frontend Files**: [Reports.jsx](file:///c:/Users/vaish/OneDrive/Desktop/social-path/frontend%20code/frontend/src/pages/Reports.jsx).
- **API Endpoints**: Calls `/scheduler` to fetch posts for client-side formatting.
- **Important Logic**: Filters posts on the client side and formats them into a downloadable CSV spreadsheet.
- **Status**: **Fully functional CSV export using client-side data**.
- **Demonstration**: Go to the Reports page, filter by LinkedIn, and click "Post Logs" to download a CSV file.

### 9. Notifications Hub
- **Problem it Solves**: Alerts the user when campaigns are initialized, posts are scheduled, or updates fail.
- **User Actions**: Clicks the sidebar bell, reads notifications, and marks them as read.
- **Frontend Files**: [Notifications.jsx](file:///c:/Users/vaish/OneDrive/Desktop/social-path/frontend%20code/frontend/src/pages/Notifications.jsx), [NotificationCard.jsx](file:///c:/Users/vaish/OneDrive/Desktop/social-path/frontend%20code/frontend/src/components/NotificationCard.jsx), [NotificationContext.jsx](file:///c:/Users/vaish/OneDrive/Desktop/social-path/frontend%20code/frontend/src/context/NotificationContext.jsx).
- **Backend Files**: [notifications.py](file:///c:/Users/vaish/OneDrive/Desktop/social-path/frontend%20code/backend/app/routers/notifications.py).
- **API Endpoints**: `GET /notifications/`, `PUT /notifications/read-all`, `PUT /notifications/{id}/read`, `DELETE /notifications/`.
- **Database Tables**: `notifications`.
- **Status**: **Fully database-backed**.
- **Demonstration**: Mark a notification as read and verify that the sidebar badge count updates.

### 10. Settings & Preferences
- **Problem it Solves**: Configures active user accounts, visual themes, localized languages, and passwords.
- **User Actions**: Updates password, switches themes, or toggles notification switches.
- **Frontend Files**: [Settings.jsx](file:///c:/Users/vaish/OneDrive/Desktop/social-path/frontend%20code/frontend/src/pages/Settings.jsx), [ThemeContext.jsx](file:///c:/Users/vaish/OneDrive/Desktop/social-path/frontend%20code/frontend/src/context/ThemeContext.jsx).
- **Backend Files**: [users.py](file:///c:/Users/vaish/OneDrive/Desktop/social-path/frontend%20code/backend/app/routers/users.py) (password updates).
- **API Endpoints**: `POST /users/change-password`.
- **Database Tables**: `users`.
- **Important Logic**: 
  - Theme state is persisted in `localStorage`.
  - Passwords are updated via the database.
  - **ALERT (Remaining Bug)**: Language selection and notification preferences (Post Success, Post Fail) are only kept in React state; they do not persist to the database or localStorage on page reload.
- **Status**: **Partially database-backed / Partially React-only state**.
- **Demonstration**: Toggle Dark Theme, refresh, and show that it persists. Update password to verify backend integration.

### 11. Global Search
- **Problem it Solves**: Allows searching across campaigns, post queues, and notifications from a single search input.
- **User Actions**: Enters a search query in the search bar.
- **Frontend Files**: Search state inside [Navbar.jsx](file:///c:/Users/vaish/OneDrive/Desktop/social-path/frontend%20code/frontend/src/components/Navbar.jsx), [searchService.js](file:///c:/Users/vaish/OneDrive/Desktop/social-path/frontend%20code/frontend/src/services/searchService.js).
- **Backend Files**: [search.py](file:///c:/Users/vaish/OneDrive/Desktop/social-path/frontend%20code/backend/app/routers/search.py).
- **API Endpoints**: `GET /search/?q={query}`.
- **Database Tables**: Searches `campaigns`, `posts`, and `notifications`.
- **Important Logic**: Filters records by both the user's ID and the search query using database `ilike` operators.
- **Status**: **Fully database-backed**.
- **Demonstration**: Search for "Summer" or "Antigravity" in the top search bar and view the grouped results.

---

## 💾 6. Database Models & Schema Mappings

The database consists of 6 tables defined in [`models.py`](file:///c:/Users/vaish/OneDrive/Desktop/social-path/frontend%20code/backend/app/models/models.py). The structure and relationships are defined below:

```text
       +------------------+
       |   User (users)   |
       +------------------+
         │   │   │   │
         │   │   │   └──────────────────────┐
         │   │   └───────────────┐          │
         │   └────────┐          │          │
         ▼            ▼          ▼          ▼
  social_accounts  campaigns   posts   notifications
                      │          │
                      │          │ (campaign_id FK)
                      └─────────►▼
                            posts
                                 │
                                 │ (post_id FK)
                                 ▼
                             analytics
```

### 1. `users` Model
- **Purpose**: Tracks credentials and user profiles.
- **Keys**: Primary Key `id` (`VARCHAR`).
- **Columns**: `username`, `email` (Unique), `password` (Hashed), `phone`, `company_name`, `avatar`, `role`, `created_at`.
- **Relationships**:
  - `social_accounts` (1:N, cascade delete)
  - `campaigns` (1:N, cascade delete)
  - `posts` (1:N, cascade delete)
  - `notifications` (1:N, cascade delete)

### 2. `social_accounts` Model
- **Purpose**: Stores linked social channels.
- **Keys**: Primary Key `id` (`UUID`). Foreign Key `user_id` (references `users.id` with `ondelete="CASCADE"`).
- **Columns**: `platform`, `account_name`, `account_id`, `access_token`, `refresh_token`, `status`, `created_at`, `updated_at`.
- **Why relationship exists**: Links connected platforms directly to the user who authorized them.

### 3. `campaigns` Model
- **Purpose**: Groups posts under specific marketing budgets and objectives.
- **Keys**: Primary Key `id` (`VARCHAR`). Foreign Key `user_id` (references `users.id` with `ondelete="CASCADE"`).
- **Columns**: `name`, `platform`, `start_date`, `end_date`, `budget`, `objective`, `performance`, `status`, `created_at`.
- **Relationships**: `posts` (1:N, cascade delete).

### 4. `posts` Model
- **Purpose**: Holds scheduled updates.
- **Keys**: Primary Key `id` (`VARCHAR`). Foreign Key `user_id` (references `users.id` with `ondelete="CASCADE"`). Foreign Key `campaign_id` (references `campaigns.id` with `ondelete="SET NULL"`).
- **Columns**: `platform`, `content`, `caption`, `media_url`, `media_type`, `status`, `scheduled_time`, `created_at`.
- **Relationships**: `analytics` (1:1, cascade delete).

### 5. `analytics` Model
- **Purpose**: Stores metrics for each post.
- **Keys**: Primary Key `id` (`VARCHAR`). Foreign Key `post_id` (references `posts.id` with `ondelete="CASCADE"`).
- **Columns**: `platform`, `likes`, `comments`, `shares`, `reach`, `impressions`, `clicks`, `recorded_at`.

### 6. `notifications` Model
- **Purpose**: Logs system alerts.
- **Keys**: Primary Key `id` (`VARCHAR`). Foreign Key `user_id` (references `users.id` with `ondelete="CASCADE"`).
- **Columns**: `title`, `message`, `type`, `is_read`, `created_at`.

---

## 🔒 7. Authentication & Security Flow

Security is implemented at both the database level (password hashing) and the communication level (JWT tokens & CORS).

```text
1. User registers
   └─► password string sent to backend
   └─► passlib[bcrypt] generates dynamic salt & hashes password
   └─► stored securely in DB (plain text is NEVER saved)

2. User logs in
   └─► submits password
   └─► bcrypt.verify compares hashed string
   └─► signs token: JWT.encode({"sub": user_id}, SECRET)

3. Frontend stores token
   └─► token saved in localStorage
   └─► Axios request interceptor attaches header: Authorization: Bearer <token>

4. Router verifies token
   └─► verify_token dependency decodes JWT signature
   └─► returns user_id
   └─► backend filters database records by user_id
```

- **Why passwords are hashed**: Ensures that even if the database is compromised, user credentials cannot be read as plain text.
- **Why JWT is used**: Enables stateless authorization. The server does not need to store session states in memory, which reduces resource usage and simplifies horizontal scaling.
- **How user isolation is achieved**: Every SQL query is scoped by the user's ID:
  `db.query(Model).filter(Model.user_id == user_id)`

---

## 🔌 8. Social Account Connect & OAuth Reality

For the purposes of this MVP, integrations are **simulated**.
1. **The Mock OAuth flow**: Clicking a connection button opens a modal requesting an account handle. Clicking "Link" saves a connection record to the database along with mock OAuth tokens.
2. **What is stored in the database**: The platform name, account handle, a generated ID, and mock token strings.
3. **What is required for real OAuth**:
   - Registering developer applications on platform developer portals (Meta, LinkedIn, Twitter/X).
   - Obtaining client credentials (Client ID, Client Secret).
   - Configuring OAuth redirect endpoints in the application.
   - Requesting and obtaining official API publishing permissions from each platform.

---

## 🔗 9. Git Branch History & Development Timeline

Below is the verified history of Git branches and key commits:

- **`feature-database`**: Mapped the SQLite engine, defined the 6 relational SQLAlchemy models, and configured UUID schemas.
  - *Key Commit*: `c599aa9` - feat: implement all 6 SQLAlchemy models with UUIDs and relationships for week 1
- **`feature-user-management`**: Implemented registration, login routers, password hashing, and token signatures.
  - *Key Commit*: `fa6f881` - Completed backend APIs and JWT authentication
- **`feature-campaign-management`**: Created campaign schema validators and campaign CRUD routers.
  - *Key Commit*: `352d815` - feat: implement campaign management module
- **`feature-scheduler`**: Integrated visual calendar libraries (FullCalendar) and configured the scheduled posts router.
  - *Key Commit*: `2195806` - Create scheduler.py
- **`feature-social-management`**: Built mock account connectors and profile database schemas.
  - *Key Commit*: `28a061a` - Completed backend development for social management module
- **`feature-frontend`**: Designed the Tailwind glassmorphic dashboard views and layout.
  - *Key Commit*: `d413d30` - feat: implement user authentication context and service modules
- **`integrated-frontend-and-backend`** *(Current)*: Integrated frontend services with backend endpoints, fixed PostgreSQL seeding issues, configured Vercel redirection rules, and prepared production build configurations.
  - *Key Commit*: `05f446e` - fix: make demo seeding safe for multi-user postgres
  - *Key Commit*: `c572ba9` - build: upgrade psycopg2-binary to 2.9.12 and pin python-version to 3.13.5 for Render deployment compatibility
  - *Key Commit*: `5cc1315` - chore: configure production database engine, postgres drivers, cors environment variables, and SPA redirection rules

---

## 🛠️ 10. Technology Stack & Selection Rationale

| Tool | Category | Where Used | Selection Rationale | Alternatives |
| :--- | :--- | :--- | :--- | :--- |
| **React** | Frontend | Core Views | Component-driven UI that renders dynamic page views without page reloads. | Angular, Vue |
| **Vite** | Build Tool | Frontend Bundler | Extremely fast development server and build tool compared to Webpack. | Webpack |
| **Tailwind CSS** | Styling | UI Styling | Utility-first styling framework that allows for rapid development of responsive layouts. | Vanilla CSS, Bootstrap |
| **FastAPI** | Backend API | REST API Gateway | Highly performant async Python framework that supports Pydantic validation and auto-generates Swagger docs. | Django, Flask |
| **SQLAlchemy** | ORM | Database Mapping | Abstracts SQL operations into Python classes, protecting against SQL injection. | Django ORM, Raw SQL |
| **PostgreSQL** | Database | Production Storage | Enterprise-grade relational database optimized for production environments. | SQLite, MySQL |
| **Supabase** | Cloud DB | DB Cloud Host | Provides managed PostgreSQL database hosting. | AWS RDS |
| **JWT** | Auth | Session Auth | Stateless tokens that eliminate the need to store session states in server memory. | Session Cookies |
| **Vercel** | Hosting | Frontend Host | Optimizes hosting for single-page applications and provides build triggers linked to GitHub. | Netlify, S3 |
| **Render** | Hosting | Backend Host | Simple cloud hosting for Python/Uvicorn applications with auto-deployments from Git. | Heroku, AWS EC2 |

---

## 🏥 11. Testing Suite Description

The test suite consists of automated tests located in `frontend code/backend/app/utils/`:

1. **Backend Integration Tests** ([`test_integration.py`](file:///c:/Users/vaish/OneDrive/Desktop/social-path/frontend%20code/backend/app/utils/test_integration.py)):
   - **What it checks**: Verifies registration, login, profile view/updates, social linking, campaigns CRUD, scheduler postings, analytics aggregation, notifications read-all, and global search.
   - **How to run**: `python app/utils/test_integration.py`
2. **Multi-User Isolation Tests** ([`test_multi_user.py`](file:///c:/Users/vaish/OneDrive/Desktop/social-path/frontend%20code/backend/app/utils/test_multi_user.py)):
   - **What it checks**: Registers two users, seeds records, and verifies that operations (GET, DELETE) performed by one user do not affect the other.
   - **How to run**: `python app/utils/test_multi_user.py`
3. **Frontend Production Build**:
   - **What it checks**: Compiles Vite resources and checks for syntax errors or build issues.
   - **How to run**: `npm run build`

---

## 🐞 12. Important Bug Fix History

### Bug 1: PostgreSQL duplicate key violation on user registration
- **Problem**: Registering a second user caused the backend to crash with an HTTP 500 error.
- **Root Cause**: The database seeding script used hardcoded primary keys (`cmp_1`, `pst_1`). When a second user registered, the database rejected inserting these keys because they were already created by the first user.
- **Fix**: Replaced hardcoded keys with dynamically generated UUID strings (`f"cmp_{uuid.uuid4().hex}"`) in the seeding script.
- **Test**: Verified by running `test_multi_user.py`.

### Bug 2: check_same_thread Connection Error in Production
- **Problem**: The backend crashed immediately when connecting to a production PostgreSQL database.
- **Root Cause**: The SQLite parameter `connect_args={"check_same_thread": False}` was passed unconditionally during engine creation in `database.py`.
- **Fix**: Updated `database.py` to apply the argument only if the database connection string starts with `sqlite`.
- **Test**: Verified by connecting to a live PostgreSQL database on Supabase.

---

## 🏆 13. Project Status & Limitations

### Status
- **GREEN**: Authentication, Profile updates, Campaigns CRUD, Calendar Scheduler views, Performance Analytics summaries, CSV Reports exports, Notifications, Search, Database models, and Multi-user isolation.
- **YELLOW (Simulated)**: Social Accounts connect (mock OAuth popup), Live post publishing (simulated updates).
- **RED (Remaining Issue)**: Language selection and notification preferences are not persisted to the database or localStorage (React state only).

### Future Enhancements
1. **Real OAuth Integrations**: Link developer apps to connect live Facebook, Instagram, LinkedIn, and Twitter/X streams.
2. **Background Workers**: Integrate Redis and Celery task queues for scheduled time publishing triggers.
3. **AI Caption Generation**: Integrate LLM suggestions for calendar media caption writes.
