# Portfolio

A personal portfolio and publishing application built with Django, Wagtail,
and React. Django provides the core site and API, Wagtail manages the blog,
and React powers the project browser.

## Stack

- Python 3.13, Django 6.0, and Wagtail 8.0
- React 18, Tailwind CSS, and Webpack
- Django REST Framework
- Docker Compose and uv

## Local setup

Install Python 3.13, [uv](https://docs.astral.sh/uv/), Node.js 24, and npm.

```bash
git clone https://github.com/freechie/portfolio-django.git
cd portfolio-django

cp -n .env.example .env

uv venv .venv --python 3.13 --clear
uv pip sync --python .venv/bin/python requirements.txt

npm ci
npm run build

npm --prefix theme/static_src ci
npm --prefix theme/static_src run build

.venv/bin/python manage.py migrate
.venv/bin/python manage.py ensure_blog
.venv/bin/python manage.py runserver
```

The application runs at [http://127.0.0.1:8000](http://127.0.0.1:8000).

## Docker

```bash
docker compose up --build
```

Docker builds both frontend bundles, applies migrations, creates the Wagtail
blog index, collects static files, and starts the local development server at
[http://127.0.0.1:8000](http://127.0.0.1:8000).

## Routes

| Path | Purpose |
| --- | --- |
| `/` | Portfolio home page |
| `/projects/` | React project browser |
| `/blog/` | Wagtail blog |
| `/api/projects/` | Project API |
| `/portal/` | Wagtail administration |
| `/dashboard/` | Django administration |

## Verification

```bash
./scripts/verify
```

The verification script installs dependencies in isolated directories, builds
the React bundle, checks migration drift, runs Django system checks, and runs
the test suite.
