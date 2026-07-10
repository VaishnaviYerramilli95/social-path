# Campaign Management Module

## Module Objective

The Campaign Management module provides the initial workflow for creating and tracking social media campaigns.

## Campaign Information

Each campaign contains:

- Campaign name
- Description
- Social media platform
- Start date
- End date
- Budget
- Objective
- Campaign status
- User ID

## Current Week 1 and Week 2 Implementation

The following functionality has been implemented:

- Campaign data model design
- Pydantic request and response schemas
- Campaign input validation
- Campaign creation API
- Campaign listing API
- Campaign details API
- Campaign update API
- Campaign deletion API
- Automatic campaign status calculation
- FastAPI route integration
- Swagger API testing
- React Campaign Management page
- React and FastAPI API integration
- CORS configuration

## Campaign Status Workflow

Campaign status is calculated using the campaign dates.

- Upcoming: Current date is before the campaign start date
- Active: Current date is between the start date and end date
- Completed: Current date is after the campaign end date

## API Endpoints

- POST /campaigns/ - Create campaign
- GET /campaigns/ - List campaigns
- GET /campaigns/{campaign_id} - Get campaign details
- PUT /campaigns/{campaign_id} - Update campaign
- DELETE /campaigns/{campaign_id} - Delete campaign

## Validation

The Campaign module validates:

- Campaign name length
- Supported social media platform
- Campaign start and end date range
- Non-negative campaign budget
- Valid UUID format for user ID

## Integration Plan

The Campaign Management module is developed in the feature-campaign-management branch.

During team integration:

- User Management will provide the authenticated user ID.
- PostgreSQL and SQLAlchemy database configuration will replace temporary in-memory campaign storage.
- Scheduler and Post modules will associate posts using campaign ID.
- Analytics will use campaign-related post metrics for campaign performance monitoring.
- Authentication and JWT middleware will protect campaign APIs.

## Pending Future Features

The following features belong to later Campaign Management development:

- Content grouping
- Advanced campaign scheduling
- Performance monitoring
- Campaign analytics
- Database persistence
- Authentication-based campaign ownership