# Relational Database Schema Documentation

This document describes the SQLite schema, tables, column types, and relational foreign keys mapped in **SocialPilot**.

---

## 📊 Database Models

### 1. `users` Table
Stores basic credentials and profile custom attributes.
- **id**: `VARCHAR` (Primary Key, generated UUID string)
- **username**: `VARCHAR` (Unique, not nullable) - holds user's full name
- **email**: `VARCHAR` (Unique, index, not nullable)
- **password**: `VARCHAR` (Hashed password payload)
- **phone**: `VARCHAR` (Nullable)
- **company_name**: `VARCHAR` (Nullable)
- **avatar**: `VARCHAR` (Nullable avatar URL string)
- **role**: `VARCHAR` (Default: `"Content Creator"`)
- **created_at**: `DATETIME` (Auto-generated UTC timestamp)

### 2. `social_accounts` Table
Stores linked social profile credentials.
- **id**: `UUID` (Primary Key, generated UUID)
- **user_id**: `VARCHAR` (Foreign Key, references `users.id` on delete Cascade)
- **platform**: `VARCHAR` (e.g. `'facebook'`, `'instagram'`, `'linkedin'`, `'twitter'`)
- **account_name**: `VARCHAR` (Social profile handle)
- **account_id**: `VARCHAR` (Unique network account reference ID)
- **access_token**: `TEXT` (OAuth key)
- **refresh_token**: `TEXT` (OAuth token)
- **status**: `VARCHAR` (Default: `"Connected"`)
- **created_at**: `DATETIME` (Auto-generated UTC timestamp)
- **updated_at**: `DATETIME` (Auto-updated UTC timestamp)

### 3. `campaigns` Table
Marketing campaigns.
- **id**: `VARCHAR` (Primary Key, generated UUID string)
- **user_id**: `VARCHAR` (Foreign Key, references `users.id` on delete Cascade)
- **name**: `VARCHAR` (not nullable)
- **platform**: `VARCHAR` (Target primary channel)
- **start_date**: `VARCHAR` (Format: `'YYYY-MM-DD'`)
- **end_date**: `VARCHAR` (Format: `'YYYY-MM-DD'`)
- **budget**: `FLOAT` (Campaign cost allotment)
- **objective**: `VARCHAR` (Description goal)
- **performance**: `VARCHAR` (e.g. `'Good'`, `'Excellent'`)
- **status**: `VARCHAR` (e.g. `'active'`, `'paused'`, `'completed'`, `'draft'`)
- **created_at**: `DATETIME` (Auto-generated UTC timestamp)

### 4. `posts` Table
Post schedules list.
- **id**: `VARCHAR` (Primary Key, generated UUID string)
- **user_id**: `VARCHAR` (Foreign Key, references `users.id` on delete Cascade)
- **campaign_id**: `VARCHAR` (Foreign Key, references `campaigns.id` on delete Set Null)
- **platform**: `VARCHAR` (e.g. `'instagram'`)
- **content**: `TEXT` (Post content / caption)
- **caption**: `TEXT` (Alias mapping for specifications)
- **media_url**: `VARCHAR` (Nullable image/video asset link)
- **media_type**: `VARCHAR` (e.g. `'image'`, `'video'`, or Null)
- **status**: `VARCHAR` (e.g. `'draft'`, `'scheduled'`, `'published'`, `'failed'`)
- **scheduled_time**: `VARCHAR` (Format: `'YYYY-MM-DDTHH:MM:00'`)
- **created_at**: `DATETIME` (Auto-generated UTC timestamp)

### 5. `analytics` Table
Stores post engagement logs.
- **id**: `VARCHAR` (Primary Key, generated UUID string)
- **post_id**: `VARCHAR` (Foreign Key, references `posts.id` on delete Cascade)
- **platform**: `VARCHAR` (Platform designation)
- **likes**: `INTEGER` (Engagement metric)
- **comments**: `INTEGER` (Engagement metric)
- **shares**: `INTEGER` (Engagement metric)
- **reach**: `INTEGER` (Audience metric)
- **impressions**: `INTEGER` (Audience metric)
- **clicks**: `INTEGER` (Conversion metric)
- **recorded_at**: `DATETIME` (UTC timestamp)

### 6. `notifications` Table
Stores user log alerts.
- **id**: `VARCHAR` (Primary Key, generated UUID string)
- **user_id**: `VARCHAR` (Foreign Key, references `users.id` on delete Cascade)
- **title**: `VARCHAR` (Headline)
- **message**: `TEXT` (Content detail)
- **type**: `VARCHAR` (e.g. `'success'`, `'info'`, `'warning'`, `'error'`)
- **is_read**: `BOOLEAN` (Default: `False`)
- **created_at**: `DATETIME` (Auto-generated UTC timestamp)
