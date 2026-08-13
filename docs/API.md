# Backend API Route Documentation

All API endpoints are hosted at `http://localhost:8000`. The OpenAPI Swagger interactive playground is accessible at `http://localhost:8000/docs`.

---

## 🔐 Authentication Module

### 1. Register User
- **Method**: `POST`
- **Endpoint**: `/auth/register`
- **Body**:
  ```json
  {
    "username": "Jane Doe",
    "email": "jane@example.com",
    "password": "securepassword",
    "phone": "+1 555-123-4567",
    "company_name": "My Business"
  }
  ```
- **Response**: JWT token details and mapped User model.

### 2. Login User
- **Method**: `POST`
- **Endpoint**: `/auth/login`
- **Headers**: `Content-Type: application/x-www-form-urlencoded`
- **Body**: Form-data containing `username` (email) and `password`.
- **Response**:
  ```json
  {
    "access_token": "eyJhbGciOiJIUzI1...",
    "token_type": "bearer",
    "user": { "id": "uuid", "username": "Jane Doe", "email": "jane@example.com" }
  }
  ```

### 3. Demo Database Seed
- **Method**: `POST`
- **Endpoint**: `/auth/seed`
- **Headers**: `Authorization: Bearer <JWT_TOKEN>`
- **Response**: `{"success": true, "message": "Demo database seeded successfully."}`

---

## 👥 Social Accounts Module
All routes require `Authorization: Bearer <JWT_TOKEN>`.

- **POST `/social-accounts/`**: Links a social channel.
- **GET `/social-accounts/`**: Lists connected channels.
- **GET `/social-accounts/{id}`**: Returns channel information.
- **DELETE `/social-accounts/{id}`**: Disconnects account.

---

## 📅 Scheduler Module
All routes require `Authorization: Bearer <JWT_TOKEN>`.

- **GET `/scheduler/`**: Returns all posts scheduled by the user.
- **POST `/scheduler/`**: Schedules a new post.
- **PUT `/scheduler/{id}`**: Updates caption content, date, time, or status of a scheduled post.
- **DELETE `/scheduler/{id}`**: Deletes a scheduled post.

---

## 📣 Campaigns Module
All routes require `Authorization: Bearer <JWT_TOKEN>`.

- **GET `/campaigns/`**: Lists campaigns created by the user.
- **POST `/campaigns/`**: Creates a campaign.
- **GET `/campaigns/{id}`**: Retrieves campaign logs.
- **PUT `/campaigns/{id}`**: Updates budget, status, performance, or objective details.
- **DELETE `/campaigns/{id}`**: Deletes a campaign.

---

## 📊 Analytics & Reporting Module
All routes require `Authorization: Bearer <JWT_TOKEN>`.

- **GET `/analytics/`**: Returns reach growth, engagement timelines, clicks, platform comparisons, and monthly followers lists.

---

## 🔔 Notifications Module
All routes require `Authorization: Bearer <JWT_TOKEN>`.

- **GET `/notifications/`**: Lists alerts.
- **PUT `/notifications/read-all`**: Marks all alerts as read.
- **PUT `/notifications/{id}/read`**: Marks a specific alert as read.
- **DELETE `/notifications/`**: Clears all alerts from the list.
- **DELETE `/notifications/{id}`**: Removes a single alert.

---

## 🔍 Global Search Module
- **GET `/search/?q=<query>`**: Requires JWT header. Returns matching campaigns, scheduled posts, and notifications in a single structured schema.

---

## 🏥 Health Module
- **GET `/health`**: Returns `{"status": "ok"}`. No auth required.
