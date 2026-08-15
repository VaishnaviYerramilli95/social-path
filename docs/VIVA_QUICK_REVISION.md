# Viva Quick Revision Sheet: SocialPilot

Read this document 30 minutes before your project review or viva. It summarizes the core aspects of the project.

---

## ⚡ 30-Second Elevator Pitch
> **"SocialPilot is a full-stack social media scheduling and campaign management dashboard. It allows marketing teams, startups, and agencies to link mock social channels, group posts under specific campaigns with budgets, and schedule updates on a visual calendar. The system isolates data per user using JWT bearer tokens, dynamically seeds realistic sample logs upon registration, aggregates analytics, and supports client-side CSV spreadsheet downloads. The backend is built using FastAPI and SQLAlchemy, while the frontend is constructed as a React SPA with Tailwind CSS."**

---

## 📐 1-Minute Architecture Summary
- **Frontend SPA**: React.js (Vite) compiles index files containing Tailwind CSS styling. Uses Axios client wrappers with request interceptors to auto-attach authorization tokens.
- **REST API Gateway**: FastAPI routers endpoints. Protects routes with token dependencies.
- **Data Mapper (ORM)**: SQLAlchemy maps database rows to python models.
- **Database Engine**: SQLite locally, migrating to PostgreSQL (Supabase) in production.
- **Multi-Tenant Scoping**: All mutations and queries filter by the user's ID to keep records isolated.

---

## 🐘 Database & Relationships
Every table in [models.py](file:///c:/Users/vaish/OneDrive/Desktop/social-path/frontend%20code/backend/app/models/models.py) references the `users` table:
- **`User` (users)**: Unique ID, username, email, hashed password.
- **`SocialAccount` (social_accounts)**: Linked profiles. Cascades on user deletion.
- **`Campaign` (campaigns)**: Marketing budget folders. Cascades on user deletion.
- **`Post` (posts)**: Scheduled caption items. Cascades on campaign/user deletion.
- **`Analytics` (analytics)**: Mapped 1:1 with posts to store reach, likes, clicks. Cascades on post deletion.
- **`Notification` (notifications)**: Bell notifications logs. Cascades on user deletion.

---

## 🔑 Security & Session Flow
1. **Registration**: Hashes password via `passlib[bcrypt]` and saves the user record.
2. **Auto-Seed**: Triggers `seed_user_data()` to insert unique mock campaigns, social accounts, and posts for the user.
3. **Login**: Verifies credentials and signs a JWT token using `python-jose` containing the user's ID.
4. **Header Auth**: The frontend stores the token in `localStorage` and appends it to subsequent request headers.
5. **Route Defense**: The backend extracts and validates the token to authenticate incoming requests.

---

## 🐞 Critical Bug Fixes Mapped
- **The Seeding Constraint Violation**:
  - *Bug*: Registering a second user caused a database crash (HTTP 500) due to duplicate campaign/post keys.
  - *Fix*: Replaced hardcoded IDs (`cmp_1`, etc.) with dynamically generated UUIDs in `seeding.py`.
- **The PostgreSQL Engine Crash**:
  - *Bug*: The backend crashed immediately on Supabase PostgreSQL.
  - *Fix*: Conditionally applied `connect_args={"check_same_thread": False}` only for SQLite connections.

---

## ❓ Top 50 Viva Questions & Answers

### General Project Q&A
1. **Q: What is the main objective of SocialPilot?**
   - **A**: To build a centralized platform for scheduling social updates and tracking campaigns.
2. **Q: Who are the target users?**
   - **A**: Startups, digital marketing agencies, content creators, and social media managers.
3. **Q: What are the main modules?**
   - **A**: Auth, Profile, Dashboard, Social Accounts, Campaigns, Scheduler, Analytics, Reports, Notifications, Settings.
4. **Q: What was your specific contribution?**
   - **A**: Designing the relational database schema, implementing FastAPI routers, integrating Axios APIs, and writing the testing suites.
5. **Q: How does the dashboard show data immediately after signup?**
   - **A**: The registration router triggers a seeding script that populates the database with realistic sample records for the user.
6. **Q: Are posts actually published to real social media networks?**
   - **A**: No, publishing is simulated. The system schedules the post in the database and updates its status to 'published' once the time passes.
7. **Q: What is a SaaS platform?**
   - **A**: Software as a Service. A cloud-hosted application model where users sign up and pay for a subscription to access software features.
8. **Q: Why is data isolation critical?**
   - **A**: It prevents users from viewing or modifying other users' campaigns or social accounts.
9. **Q: How did you test database concurrency?**
   - **A**: By writing a Python script that registers multiple users and checks for database overlaps or key collisions.
10. **Q: What happens if database seeding fails?**
    - **A**: The transaction is rolled back completely to prevent leaving partially inserted data.

### Frontend (React) Q&A
11. **Q: Why did you choose React.js?**
    - **A**: React is a component-driven framework that enables single-page application rendering, preventing page reloads.
12. **Q: What is Vite?**
    - **A**: A modern development server and bundler that is faster than traditional tools like Webpack.
13. **Q: Why Tailwind CSS?**
    - **A**: It allows for rapid styling using utility classes and supports responsive design out-of-the-box.
14. **Q: What are React Hooks?**
    - **A**: Functions like `useState` and `useEffect` that allow functional components to manage state and lifecycle events.
15. **Q: How does the frontend call the backend?**
    - **A**: Via Axios, which makes asynchronous HTTP requests to backend REST API endpoints.
16. **Q: What is an Axios Interceptor?**
    - **A**: A middleware function that runs before a request is sent, used here to automatically attach the JWT token to request headers.
17. **Q: How does the calendar work?**
    - **A**: It integrates FullCalendar to display scheduled posts on a visual grid.
18. **Q: How does dark mode work?**
    - **A**: A Tailwind theme switch toggles the `dark` class on the `<html>` element and persists the choice in `localStorage`.
19. **Q: How are graphs rendered?**
    - **A**: Using Recharts, a React charting library.
20. **Q: What is the purpose of vercel.json?**
    - **A**: It configures route rewrite rules on Vercel to route all subpaths back to `index.html`, supporting React Router SPA paths.

### Backend (FastAPI) Q&A
21. **Q: Why FastAPI?**
    - **A**: It is fast, supports asynchronous programming, uses Pydantic for validation, and auto-generates Swagger docs.
22. **Q: What is Uvicorn?**
    - **A**: An ASGI server that runs the FastAPI application.
23. **Q: What is a REST API?**
    - **A**: An API design style that uses standard HTTP methods (GET, POST, PUT, DELETE) to manipulate resources.
24. **Q: What is Pydantic?**
    - **A**: A data validation library used by FastAPI to validate incoming JSON request payloads against defined schemas.
25. **Q: What is Dependency Injection in FastAPI?**
    - **A**: A design pattern that injects dependencies (like the database session or JWT validation functions) into path operations.
26. **Q: How does `verify_token` work?**
    - **A**: It extracts the token from the request header, decodes the signature, and returns the user's ID.
27. **Q: What is a JWT token?**
    - **A**: JSON Web Token. A cryptographically signed token containing claims (like the user's ID) to manage secure sessions.
28. **Q: Why use stateless JWT over stateful sessions?**
    - **A**: JWT is stateless, meaning the server doesn't need to store session states in memory, improving scalability.
29. **Q: How do you hash passwords?**
    - **A**: Using `passlib[bcrypt]` with the Blowfish cipher.
30. **Q: What does the `/health` endpoint prove?**
    - **A**: It verifies the backend server is live and responsive.

### Database Q&A
31. **Q: Why SQLite?**
    - **A**: It is a lightweight, zero-configuration database ideal for local testing.
32. **Q: Why PostgreSQL?**
    - **A**: It is a robust relational database suited for production environments.
33. **Q: What is SQLAlchemy?**
    - **A**: An ORM that abstracts database queries, allowing developers to interact with the database using Python objects.
34. **Q: What is a database schema?**
    - **A**: The structure of database tables, columns, constraints, and relationships.
35. **Q: Explain the difference between primary keys and foreign keys.**
   - **A**: A primary key uniquely identifies a row in a table. A foreign key links a column in one table to the primary key of another.
36. **Q: What does cascade-on-delete mean?**
    - **A**: When a parent record (like a User) is deleted, all associated child records (like Campaigns and Posts) are deleted automatically.
37. **Q: What is a database transaction?**
    - **A**: A sequence of operations performed as a single logical unit of work. If any operation fails, the transaction is rolled back.
38. **Q: Why did PostgreSQL throw a UniqueViolation error in seeding?**
    - **A**: Because the initial seeding script hardcoded database primary key IDs, which caused conflicts when multiple users registered.
39. **Q: How did you fix it?**
    - **A**: By replacing hardcoded IDs with dynamically generated UUIDs in `seeding.py`.
40. **Q: What is Supabase?**
    - **A**: An open-source Firebase alternative that provides managed PostgreSQL database hosting.

### OAuth & Integrations Q&A
41. **Q: Explain what the mock OAuth connection does.**
    - **A**: It simulates account linking via a popup, generating a mock access token and saving a profile record to the database.
42. **Q: Why is OAuth mocked in this project?**
    - **A**: Real integrations require platform developer portals, official client credentials, and domain verification, which are not feasible for a student MVP.
43. **Q: What are the supported mock platforms?**
    - **A**: Facebook, Instagram, LinkedIn, and Twitter/X.
44. **Q: What is the Facebook Graph API?**
    - **A**: The primary API used to read and write data to Facebook pages and profiles.
45. **Q: What would be required to support real publishing?**
    - **A**: Real developer credentials, verified redirect URLs, and platform approval to access posting permissions.

### Deployment & Testing Q&A
46. **Q: Where is the app deployed?**
    - **A**: React frontend on Vercel, FastAPI backend on Render, PostgreSQL database on Supabase.
47. **Q: What is CORS?**
    - **A**: Cross-Origin Resource Sharing. A browser security mechanism that restricts resources on a web page from being requested from another domain.
48. **Q: How did you configure CORS?**
    - **A**: By adding a middleware in FastAPI that retrieves allowed origins from the `FRONTEND_URL` environment variable.
49. **Q: What are environment variables?**
    - **A**: Configurations stored outside the source code, used to hide secrets and database credentials.
50. **Q: What does `npm run build` do?**
    - **A**: It compiles the React source code, minifies assets, and prepares the bundle for production deployment.
