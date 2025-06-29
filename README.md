# 🌐 An Iterative Portfolio & Blog webapp

![Build Status](https://img.shields.io/badge/Build-Passing-brightgreen)
![License](https://img.shields.io/badge/License-MIT-blue)

## ✨ About the Project

This project is an **iterative full-stack web application** designed as a personal portfolio and blog. It serves as a dynamic platform to continuously showcase my evolving skills, projects, and technical expertise as a software engineer. The application features a responsive frontend built with React, a robust backend powered by Django and Django Rest Framework, and integrates strong security practices, including a nonce-based Content Security Policy.

This open-source framework provides a quick way to get a full-stack application up and running, leveraging the power of Django and React. Aspiring software engineers can utilize this project as a template to showcase their own work and administer their personal blog. While currently managed via a custom Django admin view, future iterations aim to integrate Wagtail's blogging CMS offerings. 

## 🚀 Features

*   **Responsive Design:** Crafted with Tailwind CSS for a seamless experience across all devices.
*   **Project Showcase:** Detailed descriptions and direct links to GitHub repositories for all featured projects.
*   **Integrated Blog:** A custom, self-hosted blog for technical musings and insights.
*   **Robust Security:** Implements advanced security measures including CAPTCHA, HTTPS, Rate Limiting, and a strict, nonce-based Content Security Policy (CSP).
*   **Dynamic User Interface:** A fast and interactive user experience powered by React.

## 🛠️ Technologies & Tools

**Languages:**
*   Python
*   JavaScript
*   SQL
*   Bash
*   C/C++
*   HTML/CSS

**Frontend:**
*   React
*   Tailwind CSS
*   Bootstrap

**Backend:**
*   Django
*   Django Rest Framework
*   Node.js

**Database:**
*   SQLite3

**DevOps:**
*   GitHub Actions
*   Gunicorn
*   DigitalOcean Ubuntu Server Droplet

**Developer Tools:**
*   Git
*   NeoVim
*   VS Code

**Security:**
*   Hashing
*   CAPTCHA
*   HTTPS
*   Rate Limiting
*   Content Security Policy (CSP) via `django-csp`
*   Nonce generation/handling for scripts

## ⚙️ Installation Guide

Follow these steps to set up and run the project locally.

### Prerequisites

*   **Python 3.8+**
*   **Node.js** and **npm** (or Yarn)

### Backend Setup (Django)

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/your-username/Developer-Portfolio-Platform.git
    cd Developer-Portfolio-Platform
    ```
2.  **Create a virtual environment:**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```
3.  **Install Python dependencies:**
    This project uses `pip-tools` for dependency management.
    ```bash
    pip install -r requirements.txt
    ```
    To update dependencies, modify `requirements.in` and then compile `requirements.txt`:
    ```bash
    pip-compile requirements.in
    pip install -r requirements.txt
    ```
4.  **Apply database migrations:**
    ```bash
    python manage.py migrate
    ```
5.  **Create a superuser (optional, for admin access):**
    ```bash
    python manage.py createsuperuser
    ```
6.  **Run the Django development server:**
    ```bash
    python manage.py runserver
    ```

### Frontend Setup (React)

1.  **Navigate to the frontend directory:**
    ```bash
    cd frontend
    ```
2.  **Install Node.js dependencies:**
    ```bash
    npm install # or yarn install
    ```
3.  **Build the frontend assets:**
    ```bash
    npm run build # or yarn build
    ```
    For development with hot-reloading:
    ```bash
    npm run dev # or yarn dev
    ```

### Running the Application

Ensure both the Django backend and React frontend development servers are running.

*   **Backend:** `python manage.py runserver` (usually on `http://127.0.0.1:8000/`)
*   **Frontend:** `npm run dev` (webpack will build assets and Django will serve them)

You can then access the application in your web browser at `http://127.0.0.1:8000/` (or the address where your Django server is running).