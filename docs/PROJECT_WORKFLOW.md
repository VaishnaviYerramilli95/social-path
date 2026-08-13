# Project Lifecycle Workflow

This document illustrates the lifecycle of data elements inside **SocialPilot**, detailing how elements propagate from creation to reporting.

---

## 📈 Detailed System Workflows

```text
User Registration
       │
       ▼
Auto-Seed Database ──► [Creates Campaigns, Connected Accounts, Posts]
       │
       ├─► Connect Social Account ──► [Saves Profile to DB]
       │
       ├─► Create Campaign ─────────► [Stores Budget and Objectives]
       │
       └─► Schedule Post ───────────► [Links Post to Campaign/Platform]
                                                │
                                                ▼
                                         Background Checks
                                                │
                                                ├─► Updates post status to 'published'
                                                ├─► Populates random Analytics likes/clicks
                                                └─► Sends System Notifications to User
                                                │
                                                ▼
                                        Reports & Analytics
                                                │
                                                ├─► Graph dashboards render aggregates
                                                └─► Export CSV spreadsheets & PDF prints
```

---

## 📅 Simulated Post Publishing Lifecycle

Since actual automated scheduling requires background workers (like Celery and Redis) which are outside the scope of our P0 MVP timeline, SocialPilot implements a robust database polling mechanism:
1. When a post is scheduled, its status is stored as `'scheduled'`.
2. When the backend or frontend analytics are requested, the backend performs a check on scheduled posts: if the `scheduled_time` is past the current system time, it updates the status of those posts in the database to `'published'` and spawns a corresponding `Analytics` row (with simulated likes/shares/comments) and a success `Notification`.
3. This creates a realistic simulation of a background worker, enabling live dashboard metric updates without introducing heavy, non-portable software dependencies.
