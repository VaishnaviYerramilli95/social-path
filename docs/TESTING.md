# Verification & Testing Guide

This document guides developers on how to test the **SocialPilot** codebase.

---

## 🤖 Automated Integration Testing

We have built an integration test suite that programmatically tests all REST API endpoints.

To run the test suite, activate your Python virtual environment and run the test script:

```bash
cd "frontend code"
.\venv\Scripts\python.exe backend\app\utils\test_integration.py
```

### API Coverage verified by the script:
1. **User Authentication**: User Registration (`POST /auth/register`) and User Login (`POST /auth/login`).
2. **User Profiles**: Profile Fetching (`GET /users/profile`) and Profile Updates (`PUT /users/{id}`).
3. **Social Account Module**: Linking profiles (`POST /social-accounts/`), fetching synced lists (`GET /social-accounts/`), and deleting links (`DELETE /social-accounts/{id}`).
4. **Campaign Module**: Campaign creation (`POST /campaigns/`) and fetching lists (`GET /campaigns/`).
5. **Scheduler Module**: Scheduling posts (`POST /scheduler/`) and fetching listings (`GET /scheduler/`).
6. **Analytics Engine**: Metric aggregation (`GET /analytics/`).
7. **Notification Hub**: Reading alerts (`GET /notifications/`) and updating states (`PUT /notifications/{id}/read`).
8. **Global Search**: Query filters (`GET /search/?q=test`).
9. **Health Check**: Endpoint ping checks (`GET /health`).

---

## 🧪 Manual Frontend Verification Checklist

1. **Sign-up & Seeding**:
   - Register a new account at `/register`.
   - Confirm you are redirected to the `/dashboard`.
   - Verify that your sidebar shows your company name and avatar, and the dashboard already contains 4 connected profiles and active campaign summaries.
2. **Connect Account**:
   - Navigate to `/social-accounts`.
   - Click a platform, type in a handle name, and click **Authorize & Link**.
   - Verify that the card displays a checkmark indicating connection.
3. **Schedule Content**:
   - Navigate to `/scheduler`.
   - Select a date on the calendar, insert a post caption, choose your time, and save.
   - Verify that the calendar updates dynamically.
4. **Download Report**:
   - Navigate to `/reports`.
   - Apply a platform or campaign filter.
   - Click **Campaigns** or **Post Logs** under Quick Exports and verify that the CSV downloaded contains valid comma-separated rows.
