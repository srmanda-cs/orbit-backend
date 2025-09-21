# Orbit Backend

[![License: AGPL v3](https://img.shields.io/badge/License-AGPL%20v3-blue.svg)](https://www.gnu.org/licenses/agpl-3.0)

Backend API for Orbit - my personal calendar management system.

## What is this?

FastAPI backend that will:

- Manage calendar events
- Sync with external calendars (Google, Outlook)
- Handle booking requests
- Archive old events automatically

## Tech Stack

- **FastAPI** - Python web framework
- **PostgreSQL** - Database
- **SQLAlchemy** - ORM
- **Railway** - Deployment

## Setup

```bash
# Clone and setup
git clone https://github.com/srmanda-cs/orbit-backend.git
cd orbit-backend
git checkout development
python setup_env.py

# Get your DATABASE_URL from your Postgres provider and add to .env files

# Install
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\Activate.ps1
pip install -r requirements.txt

# Run migrations
alembic upgrade head

# Run
uvicorn app.main:app --reload
```

API docs: [http://localhost:8000/docs](http://localhost:8000/docs)

## Branches

- **master** - Production (auto-deploys to Railway)
- **development** - Active Development

## Frontend

Serves [orbit-frontend](https://github.com/srmanda-cs/orbit-frontend?tab=readme-ov-file)

## Author

[@srmanda-cs](https://github.com/srmanda-cs)
