# Turistei API

Backend API for **Turistei**, a travel-planning application that helps users discover attractions, register preferences, receive recommendations, organize schedules, and submit new-attraction requests.

This repository contains the Python backend that supports the Turistei web client.

## Tech stack

- **Python 3**
- **FastAPI** for HTTP APIs and automatic OpenAPI documentation
- **SQLAlchemy** for relational persistence
- **PostgreSQL** as the primary database
- **Alembic** for database migrations
- **Pydantic** for request/response validation
- **Passlib + bcrypt** for password hashing
- **Uvicorn** as the ASGI server

## Main capabilities

The API is organized into routers, schemas, services, models, and database infrastructure rather than concentrating business logic in a single module.

Current domains include:

- **Users** — registration, lookup, and credential validation
- **Places** — tourism-place data
- **Preferences** — user travel preferences
- **Recommendations** — recommendation endpoints based on application data
- **Schedules** — itinerary/schedule management
- **Attraction requests** — requests for new attractions to be added to the platform

FastAPI exposes interactive API documentation automatically at `/docs` when the service is running.

## Project structure

```text
.
├── alembic/                 # Database migrations
├── app/
│   ├── api/
│   │   ├── core/            # Shared application configuration
│   │   ├── models/          # SQLAlchemy models
│   │   ├── routers/         # HTTP route modules
│   │   ├── schemas/         # Pydantic schemas
│   │   ├── services/        # Application/domain services
│   │   ├── database.py      # Database session/engine setup
│   │   └── main.py          # FastAPI application entry point
│   ├── security.py          # Password hashing and verification
│   └── tests/               # Test package
├── alembic.ini
├── requirements.txt
└── .env.example
```

## Running locally

### 1. Clone the repository

```bash
git clone https://github.com/joaoplima04/TuristeiAPI.git
cd TuristeiAPI
```

### 2. Create a virtual environment

```bash
python -m venv .venv
```

Activate it:

```bash
# macOS/Linux
source .venv/bin/activate

# Windows PowerShell
.venv\Scripts\Activate.ps1
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure the database

Copy the example environment file and update the connection string for your local PostgreSQL instance:

```bash
cp .env.example .env
```

On Windows, create `.env` manually from `.env.example` if `cp` is unavailable.

### 5. Start the API

```bash
uvicorn app.api.main:app --reload
```

Then open:

- API: `http://localhost:8000`
- Swagger UI: `http://localhost:8000/docs`
- OpenAPI schema: `http://localhost:8000/openapi.json`

## API design

The application uses FastAPI routers to keep endpoint groups separated by domain. Database access is handled through SQLAlchemy sessions, while Pydantic schemas define external request/response contracts.

Passwords are not stored in plaintext; password hashing and verification use bcrypt through Passlib.

## Database migrations

Alembic configuration is included in the repository. When changing persistent models, migrations should be created and reviewed rather than relying only on implicit schema creation.

Typical workflow:

```bash
alembic revision --autogenerate -m "describe change"
alembic upgrade head
```

## Engineering notes

This project is part of a broader full-stack application. The frontend lives in the companion repository [`joaoplima04/turistei`](https://github.com/joaoplima04/turistei).

The repository is also being used as a portfolio project, so cleanup is intentionally focused on making architecture, setup, security decisions, and ownership easier to evaluate without changing application behavior.

## Author

**João Lucas**  
Full-stack software engineer focused on Python/FastAPI, TypeScript/Next.js, PostgreSQL, API integrations, cloud infrastructure, and secure software development.

- GitHub: [@joaoplima04](https://github.com/joaoplima04)
