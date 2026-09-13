# Sales AI Agent V1

Sales AI Agent V1 is a foundation for an incremental sales workflow system. The long-term goal is to help users find leads, research companies, qualify and score opportunities, generate outreach for human approval, and eventually coordinate CRM and email workflows.

V1 intentionally implements only the runnable foundation and first agent architecture skeleton.

## Architecture

```text
apps/
  api/        FastAPI backend
  web/        Next.js frontend
agents/       LangGraph sales agent foundation
core/         configuration, database, schemas, logging, security
integrations/ reserved for future external integrations
memory/       reserved for short-term, long-term, and vector memory
tools/        reserved for controlled external actions
tests/        backend and agent tests
```

The initial agent layer contains:

- Sales Orchestrator
- Research Agent
- Qualification Agent
- Outreach Agent

## Technology Stack

- Frontend: Next.js, TypeScript, App Router
- Backend: Python, FastAPI
- Agent orchestration: LangGraph
- Database: PostgreSQL with pgvector image
- Migrations: Alembic
- Testing: Pytest
- Local infrastructure: Docker Compose

## Environment Variables

Copy `.env.example` to `.env` for local development:

```text
OPENAI_API_KEY=your-openai-api-key
DATABASE_URL=postgresql+psycopg://sales_agent:sales_agent@localhost:5432/sales_agent
```

Do not commit real secrets.

## Backend Setup

```bash
python -m venv .venv
.venv\Scripts\activate
python -m pip install -e ".[dev]"
uvicorn apps.api.app.main:app --reload
```

Health check:

```bash
curl http://127.0.0.1:8000/health
```

## Frontend Setup

```bash
cd apps/web
npm install
npm run dev
```

The frontend starts at `http://localhost:3000`.

## PostgreSQL

```bash
docker compose up -d postgres
```

The database is available at `localhost:5432`.

## Alembic

Run migrations:

```bash
alembic upgrade head
```

Create a future migration:

```bash
alembic revision --autogenerate -m "describe change"
```

## Tests

```bash
pytest
```

## Current V1 Limitations

- No Gmail, HubSpot, WhatsApp, LinkedIn, or n8n integration is implemented.
- No autonomous outreach or email sending exists.
- No production business schema has been created yet.
- Agent implementations are minimal and deterministic placeholders designed for expansion.
