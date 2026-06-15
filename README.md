# Pixel Forge

A small asset-pipeline SaaS for indie game studios: upload, optimize, version, and
serve art/sprite assets via an API. Built with **FastAPI + SQLModel + Alembic +
Postgres + Redis**.

This repository is the workspace for the **DevAscent — Hardcore Mode** career
simulation. You fork it, clone your fork, and work the board ticket-by-ticket: pick a
ticket → fix it → tests pass → open a PR → CI gates it → the next unlocks.

## Run it

The early tickets are pure Python and need only Python + pytest:

```sh
python -m venv .venv && . .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r requirements.txt
pytest                                          # the visible test suite
```

The full stack (Postgres + Redis, needed from the database tickets onward) comes up
with Docker:

```sh
cp .env.example .env
docker compose up -d
alembic upgrade head
```

## Layout

```
pixelforge/
  core/      pure helpers (pagination, slugs, human sizes, safe filenames, …)
  api/       FastAPI routers (assets, auth, billing)
  models/    SQLModel + Alembic migrations          (added from the DB tickets)
  workers/   image optimize / thumbnail jobs (Redis) (added from the worker tickets)
tests/       the visible unit tests you run yourself
```

Hidden acceptance tests run in CI (and in the DevAscent app) — they are not in this
repository, exactly like a real job: you build to the acceptance criteria; QA/CI runs
more checks you don't control.
