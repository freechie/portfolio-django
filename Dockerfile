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
    libpq-dev \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Install uv
COPY --from=ghcr.io/astral-sh/uv:latest /uv /bin/uv

# Copy requirements files
COPY requirements.txt requirements-wagtail.txt /app/

# Install python dependencies using uv
RUN uv pip install --system -r requirements.txt -r requirements-wagtail.txt

# Copy project
COPY . /app/

# Create a non-root user and switch to it
RUN adduser --disabled-password --gecos '' django
RUN chown -R django:django /app
USER django

# Expose port
EXPOSE 8000

# Command to run the application
CMD ["gunicorn", "portfolio.wsgi:application", "--bind", "0.0.0.0:8000"]

