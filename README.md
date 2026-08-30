# 🌐 Developer Portfolio & Blog

A high-performance, secure personal portfolio and blog platform built with **Django 6.0**, **Wagtail CMS**, and **React**.

## ✨ Features

- **Responsive Showcase:** Project portfolio with GitHub integration and image carousels.
- **Wagtail CMS:** Fully integrated blogging engine for technical content.
- **Production Hardened:** Pre-configured with CSP (Nonces), Rate Limiting, Brute-force protection, and Deep File Validation.
- **Modern Tooling:** Powered by `uv` for lightning-fast dependency management and `Docker` for easy deployment.

## 🚀 Quick Start

### 1. Local Setup (with `uv`)

Ensure you have [uv](https://github.com/astral-sh/uv) installed.

```bash
# Clone and enter the repo
git clone https://github.com/freechie/portfolio-django.git
cd portfolio-django

# Create the pinned Python environment and install dependencies
uv venv .venv --python 3.13 --clear
uv pip sync --python .venv/bin/python requirements.txt

# Install and build the React bundle
npm ci
npm run build

# Configure the application, then run migrations
cp -n .env.example .env
.venv/bin/python manage.py migrate
.venv/bin/python manage.py ensure_blog

# Start development server
.venv/bin/python manage.py runserver
```

Run the complete verification suite with `./scripts/verify`.

### 2. Docker Setup (Recommended)

The easiest way to get started is using Docker Compose, which handles all dependencies and environment setup.



```bash

# Build and start the container

docker-compose up --build

```

*   The application will be available at `http://localhost:8000`.

*   The setup automatically runs migrations and collects static files on startup.



## 🛠️ Tech Stack

- **Backend:** Python 3.13, Django 6.0, Wagtail CMS, Django Rest Framework.
- **Frontend:** React, Tailwind CSS, DaisyUI, Webpack.
- **Infrastructure:** Docker, uv, Gunicorn, WhiteNoise.
- **Security:** django-csp (Nonces), django-axes (Lockout), django-ratelimit, python-magic (MIME validation).

## 🔑 Administration

- **Django Admin:** `/dashboard/`
- **Wagtail CMS:** `/portal/`

---

© 2026 John R. Molina
