# 🌐 Developer Portfolio & Blog

A high-performance, secure personal portfolio and blog platform built with **Django 6.0**, **Wagtail CMS**, and **React**.

## ✨ Features

*   **Responsive Showcase:** Project portfolio with GitHub integration and image carousels.
*   **Wagtail CMS:** Fully integrated blogging engine for technical content.
*   **Production Hardened:** Pre-configured with CSP (Nonces), Rate Limiting, Brute-force protection, and Deep File Validation.
*   **Modern Tooling:** Powered by `uv` for lightning-fast dependency management and `Docker` for easy deployment.

## 🚀 Quick Start

### 1. Local Setup (with `uv`)
Ensure you have [uv](https://github.com/astral-sh/uv) installed.

```bash
# Clone and enter the repo
git clone https://github.com/your-username/Developer-Portfolio-Platform.git
cd Developer-Portfolio-Platform

# Sync environment and run migrations
uv pip sync requirements.txt requirements-wagtail.txt
python manage.py migrate

# Start development server
python manage.py runserver
```

### 2. Docker Setup
```bash
docker-compose up --build
```
Access the app at `http://localhost:8000`.

## 🛠️ Tech Stack

*   **Backend:** Python 3.13, Django 6.0, Wagtail CMS, Django Rest Framework.
*   **Frontend:** React, Tailwind CSS, DaisyUI, Webpack.
*   **Infrastructure:** Docker, uv, Gunicorn, WhiteNoise.
*   **Security:** django-csp (Nonces), django-axes (Lockout), django-ratelimit, python-magic (MIME validation).

## 🔑 Administration
*   **Django Admin:** `/dashboard/`
*   **Wagtail CMS:** `/portal/`

---
© 2026 John R. Molina
