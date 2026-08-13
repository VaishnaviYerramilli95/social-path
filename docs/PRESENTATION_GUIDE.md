# Mentoring Presentation & Demonstration Script

This presentation guide provides a script and answers to common technical questions to assist in demonstrating **SocialPilot**.

---

## 🎭 Live Demonstration Script (5-Minute Walkthrough)

### 1. The Opening Hook (1 Minute)
> "Good morning/afternoon. Today I am presenting SocialPilot, a centralized SaaS dashboard designed to solve the chaotic problem of social media management. Content creators, marketing teams, and brands struggle with scattered postings, disconnected analytics, and manual coordination. Our solution consolidates registration, oauth simulations, scheduler queues, and performance reports into a single, cohesive, premium SaaS platform."

### 2. Registration and Automatic Seeding (1.5 Minutes)
> "Let's begin by registering a new user. As a developer/presenter, manually entering dozens of records to show off a dashboard is slow and tedious. To address this, SocialPilot has a built-in auto-seeding system. The moment I click 'Register', our backend database creates a clean state and immediately seeds realistic campaigns, connected accounts, post logs, and past analytics. Here we are on the Dashboard: we immediately see total scheduled counts, active campaign spend charts, and recent activity logs fetched directly from our SQLite database."

### 3. Connect a Social Profile (1 Minute)
> "Next, let's look at profile management. If I go to the 'Social Accounts' tab, I can see what channels are linked. Let's add a new Instagram Business page. By entering a profile handle and clicking 'Authorize', we trigger a simulated OAuth consent screen that stores a real connection record in our database. The dashboard count updates instantly."

### 4. Create and Schedule Updates (1 Minute)
> "In the 'Scheduler' page, we see a premium custom calendar displaying posts. Let's schedule a new post for next Wednesday. We enter a caption, set the time, and click 'Schedule'. The post is immediately persisted to the DB and rendered on the calendar grid."

### 5. Aggregate Analytics and Exports (0.5 Minutes)
> "Under 'Analytics' and 'Reports', users get a unified look at their click CTR, follower metrics, and campaign budget spend. In the 'Reports' tab, we can filter our logs by platform or campaign and trigger a one-click CSV export, downloading formatted records instantly."

---

## ❓ Frequently Asked Questions & Answers

### Q: Why React.js for the Frontend?
> "React's modular, state-driven design is ideal for building highly interactive single-page applications. It allows us to manage complex component states (like calendar cell overlays, drag-drop mock uploads, and dynamic table filters) cleanly without page-refresh overhead."

### Q: Why FastAPI for the Backend?
> "FastAPI is extremely fast, fully supports asynchronous concurrency, and utilizes Pydantic for automated request/response payload validation. It also self-documents all endpoints via Swagger, speeding up development and integration testing."

### Q: How does session verification work?
> "When a user logs in, the backend signs a JSON Web Token (JWT) with their ID. This token is stored in the frontend's localStorage. The Axios instance acts as a gateway interceptor, attaching the bearer token to all outgoing headers. The backend protects routes using a `verify_token` dependency that decodes and validates the token signature before resolving requests."

### Q: How is database multi-tenancy handled?
> "Every database table (Campaigns, Posts, SocialAccounts, Notifications) has a `user_id` foreign key referencing the `users` table. The backend verifies the requester's identity via JWT and filters all operations on `(id, user_id)` to ensure users can only access their own records."

### Q: How does scheduling automation work in this MVP?
> "In this MVP, rather than running heavy background celery worker processes, the backend performs a check when analytics or scheduler queues are queried. If a post's scheduled timestamp is in the past, its status is updated to 'published' in the DB, and corresponding analytics logs are generated. This delivers a reliable, lightweight simulation of automated publishing."
