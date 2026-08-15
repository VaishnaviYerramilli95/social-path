# Screen-Share Presentation Script: SocialPilot

Use this script during your final review or viva. It is written to sound like a student talking naturally while demoing their own project.

---

## 🧭 1. Introduction
- **On Screen**: Login page (`/login`).
- **What to Say**:
  > "Good morning/afternoon, respect mentors. Today, I am presenting my final-year project, 'SocialPilot'. This is a centralized dashboard for social media campaign organization, scheduler posting, and multi-tenant performance analytics tracking. My objective was to build a clean, responsive web application that streamlines social workflows, connects posts to financial campaigns, and scopes all data per user using secure tokens."

## ⚠️ 2. Problem
- **On Screen**: Still on `/login`.
- **What to Say**:
  > "The main problem this solves is fragmentation. Right now, creators and marketing agencies have to log into Facebook, Instagram, LinkedIn, and Twitter/X separately to post. They also track budgets in separate spreadsheets, and combine metrics manually. This takes hours, and is highly prone to copy-paste errors. Plus, agencies need strict database isolation so client data doesn't leak."

## 🚀 3. Solution
- **On Screen**: Still on `/login`.
- **What to Say**:
  > "SocialPilot brings all of this together. It groups post queues under specific marketing campaigns with budgets, tracks reaches/likes/clicks in a single database, and displays visual schedules on a calendar grid. By using stateless JWT validation, we achieve strict multi-tenant isolation, meaning each user's campaigns and tokens are completely private."

## 📐 4. Architecture
- **On Screen**: Still on `/login` (or open the OpenAPI `/docs` page in another tab briefly).
- **What to Say**:
  > "Technically, the project uses a fully decoupled client-server architecture. The frontend is a React single-page application built with Vite and Tailwind CSS. The backend is an asynchronous REST API built with FastAPI in Python. For the database, we use SQLAlchemy ORM. In local development we run SQLite, and in production we deploy a PostgreSQL database on Supabase."

## 🔑 5. Login
- **On Screen**: Switch to `/login`.
- **What to Do**:
  - Enter the username of a previously registered user or click **Register** to create a new one. (Let's register `vaish_tester@example.com`).
- **What to Say**:
  > "Let's log in to the system. The authentication uses JSON Web Tokens. When I type the email and password, the frontend calls the `/auth/login` endpoint. The backend verifies the password using the bcrypt hashing algorithm. If it matches, the server returns a signed JWT token which the frontend stores in `localStorage` and automatically attaches to all future headers."

## 📊 6. Dashboard
- **On Screen**: Redirected to `/dashboard`.
- **What to Do**:
  - Point to the metrics cards at the top.
  - Point to the quick stats (Total Posts, Scheduled, Published, Failed, Active Campaigns).
- **What to Say**:
  > "This is our main Dashboard. We see our key metric summaries immediately. The dashboard gathers stats by querying the database for connected channels, campaigns, and scheduled posts owned by my user ID. Because of our multi-tenant design, these counts represent my data only."

## 👥 7. Social Accounts
- **On Screen**: Click **Social Accounts** in the sidebar.
- **What to Do**:
  - Hover over the platform connection buttons.
  - Point to the "Mock OAuth Connections Enabled" warning banner.
  - Click **Instagram Profile**, type `@brand_insta`, and click **Authorize & Link**.
- **What to Say**:
  > "In the Social Accounts tab, we connect our profiles. For this MVP, we have implemented simulated OAuth popup modals. Connecting to real social media APIs requires company developer applications, verified redirect domains, and client credentials, which are not accessible for college testing. The mock flow generates a simulated access token and saves the record in our database."

## 📅 8. Campaigns
- **On Screen**: Click **Campaigns** in the sidebar.
- **What to Do**:
  - Click **+ New Campaign**.
  - Fill in the form: Name: `Holiday Launch`, Platform: `Instagram`, Budget: `5000`, Objective: `Driving winter holiday discount sales`.
  - Click **Create Campaign**.
- **What to Say**:
  > "Next, let's look at the Campaign module. We can create marketing campaigns to organize our postings and track budgets. Let's create one called 'Holiday Launch' with a budget of 5000 and select Instagram. When I submit, it saves a campaign row linked to my user ID."

## 📅 9. Scheduler
- **On Screen**: Click **Scheduler** in the sidebar.
- **What to Do**:
  - Double-click a calendar grid square.
  - Fill in the modal: Platform: `Instagram`, Caption: `Get 30% off our products today!`, Campaign: Select `Holiday Launch` from the dropdown, Time: `15:30`.
  - Click **Schedule Post**.
- **What to Say**:
  > "Now, we go to the Scheduler. This visual calendar uses FullCalendar. If I double-click any date, it opens the scheduler form. I can write my caption, link it to my new 'Holiday Launch' campaign, select the platform, and schedule it. The post appears instantly on the calendar grid. In the database, its status is stored as 'scheduled' and publishing is simulated."

## 📊 10. Analytics
- **On Screen**: Click **Analytics** in the sidebar.
- **What to Do**:
  - Scroll through the charts (Monthly Growth, Platform Comparison, Weekly Rates).
- **What to Say**:
  > "Under Analytics, the app generates graphs using Recharts. The backend retrieves the posts I've scheduled, aggregates metrics from the `analytics` table, and calculates totals. If a new user has no metrics yet, the API applies a dynamic fallback calculation to prevent blank dashboard displays during demonstration."

## 📊 11. Reports
- **On Screen**: Click **Reports** in the sidebar.
- **What to Do**:
  - Select `Instagram` from the platform filter dropdown.
  - Click **Post Logs** under Quick Exports and verify the CSV downloads.
- **What to Say**:
  > "In the Reports tab, we can filter our schedules by platform or campaign. We can also click 'Post Logs' to trigger a client-side CSV download. This formats our database records into a clean spreadsheet structure for offline review."

## 🔔 12. Notifications
- **On Screen**: Click the Bell icon in the sidebar or go to `/notifications`.
- **What to Do**:
  - Show the notification card deck.
  - Click **Mark as Read** on a card and point to the sidebar counter updating.
- **What to Say**:
  > "We also have a system Notifications Hub. Whenever campaigns are created, posts are scheduled, or connections are updated, the system inserts alert logs in the database. When I mark them as read, the backend updates the `is_read` boolean, and our badge count refreshes."

## ⚙️ 13. Settings
- **On Screen**: Click **Settings** in the sidebar.
- **What to Do**:
  - Toggle the **Dark Theme Palette** switch to show the immediate color change.
  - Toggle it back to Light.
- **What to Say**:
  > "In the Settings tab, we can configure our workspace. The Dark Theme switches Tailwind classes dynamically and stores the selection in `localStorage` so it persists after refresh.
  > 
  > *NOTE*: For the sake of transparency, settings like language selection and email subscription switches are kept in temporary React state and do not persist to the database yet. Password updates, however, are fully connected to our backend."

## 💾 14. Database
- **On Screen**: Point to the SQLite file or visual ER tree schema if you have slides.
- **What to Say**:
  > "Our database schema contains 6 tables: Users, SocialAccounts, Campaigns, Posts, Analytics, and Notifications. All models are related via user_id foreign keys, and posts map to campaigns via campaign_id foreign keys. We've set up cascades so that deleting a user clean-deletes all associated campaigns and posts."

## ⚙️ 15. Backend
- **On Screen**: Open your code editor showing [main.py](file:///c:/Users/vaish/OneDrive/Desktop/social-path/frontend%20code/backend/app/main.py).
- **What to Say**:
  > "The FastAPI backend uses asynchronous endpoints for speed. We define input and output schemas using Pydantic, which validates data structures before database operations. This prevents corrupt data entry."

## 🚀 16. Deployment
- **On Screen**: Switch back to the web browser.
- **What to Say**:
  > "The application is fully deployed. The React frontend is hosted on Vercel, which hooks into our GitHub repository. The FastAPI server is hosted on Render, and our PostgreSQL database is hosted on Supabase. CORS headers are configured on Render so Vercel can safely call the API."

## 🧪 17. Testing
- **On Screen**: Show the test files in your IDE: [`test_integration.py`](file:///c:/Users/vaish/OneDrive/Desktop/social-path/frontend%20code/backend/app/utils/test_integration.py) and [`test_multi_user.py`](file:///c:/Users/vaish/OneDrive/Desktop/social-path/frontend%20code/backend/app/utils/test_multi_user.py).
- **What to Say**:
  > "We wrote automated backend tests. `test_integration.py` verifies all CRUD endpoints. `test_multi_user.py` checks database isolation, registering two users and asserting that User 1's actions do not affect User 2's data rows."

## ⚠️ 18. Limitations
- **On Screen**: Navigate back to Settings.
- **What to Say**:
  > "The primary limitation of this MVP is that publishing is simulated rather than posted to live social streams. Additionally, settings preferences like language and alert alerts are React state only and do not persist to the database."

## 🚀 19. Future Scope
- **On Screen**: Still on Settings page.
- **What to Say**:
  > "For future work, we plan to implement background worker queues using Celery and Redis to handle automated publishing. We also want to integrate official developer API keys for Facebook and Twitter, and add an AI caption generator using OpenAI or Gemini models."

## 🏁 20. Conclusion
- **On Screen**: Click **Logout Session** on the sidebar.
- **What to Say**:
  > "To conclude, SocialPilot successfully achieves campaign relations, visual scheduling, analytics aggregates, and multi-user data security. I've logged out, which clears our JWT token. Thank you very much, and I'm happy to answer any questions."
