FROM node:24-alpine AS frontend-builder

WORKDIR /app

COPY package.json package-lock.json webpack.config.js .babelrc /app/
RUN npm ci

COPY frontend /app/frontend
RUN npm run build

# Build the ignored Tailwind output so a fresh clone does not depend on a
# developer's local theme/static/css/dist directory.
COPY theme/static_src/package.json theme/static_src/package-lock.json /app/theme/static_src/
RUN npm --prefix theme/static_src ci
COPY . /app/
RUN npm --prefix theme/static_src run build

# Use an official Python runtime as a parent image
FROM python:3.13-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set work directory
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    libmagic1 \
    libpq-dev \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Install uv
COPY --from=ghcr.io/astral-sh/uv:0.11.29 /uv /bin/uv

# Copy the locked requirements
COPY requirements.txt /app/

# Install python dependencies using uv
RUN uv pip install --system -r requirements.txt

# Copy project
COPY . /app/

# Copy the built React assets from the frontend stage.
COPY --from=frontend-builder /app/frontend/static/frontend /app/frontend/static/frontend

# Copy the built Tailwind stylesheet from the frontend stage.
COPY --from=frontend-builder /app/theme/static/css/dist /app/theme/static/css/dist

# Create a non-root user and switch to it
RUN adduser --disabled-password --gecos '' django
RUN chown -R django:django /app
USER django

# Expose port
EXPOSE 8000

# Command to run the application
CMD ["gunicorn", "portfolio.wsgi:application", "--bind", "0.0.0.0:8000"]
