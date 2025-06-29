import os
import environ
from pathlib import Path

# ==============================================================================
# ENVIRONMENT CONFIGURATION
# ==============================================================================
# Initialize django-environ. This helps manage environment variables gracefully.
# Here, we specify that the DEBUG variable should be cast to a boolean and
# will default to False if not found in the environment.
env = environ.Env(
    DEBUG=(bool, False)
)

# Define the project's base directory (the folder containing manage.py).
# `Path(__file__).resolve()` gets the path to this settings.py file.
# `.parent.parent` moves up two levels to the project root.
BASE_DIR = Path(__file__).resolve().parent.parent

# Instruct django-environ to read the .env file located in the project's root.
# This loads the key-value pairs from the file into the environment, making them
# accessible via `env('VARIABLE_NAME')`.
environ.Env.read_env(os.path.join(BASE_DIR, '.env'))


# ==============================================================================
# CORE DJANGO SETTINGS
# ==============================================================================
# The secret key for cryptographic signing. Loaded from the .env file for security.
# This app will not start if the key is missing.
SECRET_KEY = env('DJANGO_SECRET_KEY')

# Debug mode. Loaded from .env (e.g., DEBUG=True).
# Crucially, this should ALWAYS be False in a production environment.
DEBUG = env("DEBUG")

# A list of host/domain names that this Django site can serve.
# This is a security measure to prevent HTTP Host header attacks.
ALLOWED_HOSTS = ['localhost', '[::1]', '127.0.0.1']


# ==============================================================================
# APPLICATIONS AND MIDDLEWARE
# ==============================================================================
# A list of all Django applications activated in this project.
INSTALLED_APPS = [
    # Third-party apps - generally loaded first
    "webpack_loader",

    # Your project's local apps
    "django_portion.apps.DjangoPortionConfig",

    # Core Django apps
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "whitenoise.runserver_nostatic",  # Makes `runserver` behave like production for static files
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",

    # More third-party apps
    "taggit",
    "rest_framework",
    "tailwind",
    "corsheaders",
    "captcha",
    "csp",

    # Your local theme app
    "theme",

    # Example of a development-only app, commented out for production
    # "django_browser_reload",
]

# Middleware processes requests and responses globally. The order is critical.
MIDDLEWARE = [
    # Handles Cross-Origin Resource Sharing (CORS) headers. Should be high up.
    "corsheaders.middleware.CorsMiddleware",
    # Adds several security enhancements. Should be near the top.
    "django.middleware.security.SecurityMiddleware",
    # Serves static files efficiently in production. Placed after SecurityMiddleware.
    "whitenoise.middleware.WhiteNoiseMiddleware",
    # Manages user sessions across requests.
    "django.contrib.sessions.middleware.SessionMiddleware",
    # Custom middleware for your project.
    "django_portion.middleware.NonceMiddleware",
    # Adds common headers and handles other basic web tasks.
    "django.middleware.common.CommonMiddleware",
    # Adds protection against Cross-Site Request Forgery.
    "django.middleware.csrf.CsrfViewMiddleware",
    # Associates users with requests using sessions.
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    # Enables cookie- and session-based messaging.
    "django.contrib.messages.middleware.MessageMiddleware",
    # Protects against clickjacking by using the X-Frame-Options header.
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    # Middleware for Content Security Policy.
    "csp.middleware.CSPMiddleware",

    # Example of a development-only middleware, commented out for production
    # "django_browser_reload.middleware.BrowserReloadMiddleware",
]

# The root URL configuration module for the project.
ROOT_URLCONF = "portfolio.urls"

# Configuration for Django's template engine.
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / 'templates'],  # A project-level directory for templates
        "APP_DIRS": True,  # Looks for templates inside individual app directories
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                "django.template.context_processors.media",
            ],
        },
    },
]

# The entry-point for WSGI-compatible web servers to serve your project.
WSGI_APPLICATION = "portfolio.wsgi.application"


# ==============================================================================
# DATABASE
# ==============================================================================
# Database configuration. This example uses SQLite, which is file-based.
# For production, you would typically use a DATABASE_URL from your .env file.
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}


# ==============================================================================
# AUTHENTICATION AND PASSWORDS
# ==============================================================================
# A list of validators used to check the strength of users' passwords.
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators
AUTH_PASSWORD_VALIDATORS = [
    {"NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"},
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]


# ==============================================================================
# INTERNATIONALIZATION (I18N)
# ==============================================================================
# https://docs.djangoproject.com/en/5.0/topics/i18n/
LANGUAGE_CODE = "en-us"
# NOTE: It's best practice to use "UTC" for TIME_ZONE to store all data consistently.
# The server can then convert to the user's local time zone for display.
TIME_ZONE = "EST"
USE_I18N = True  # Enable Django's translation system.
USE_TZ = True  # Makes Django's datetimes timezone-aware.


# ==============================================================================
# STATIC AND MEDIA FILES
# ==============================================================================
# URL to use when referring to static files (CSS, JavaScript, Images).
STATIC_URL = "/static/"
# The absolute path to the directory where `collectstatic` will gather all static files
# for deployment. WhiteNoise uses this directory in production.
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
# The storage backend for static files, configured for WhiteNoise's compression.
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# The absolute filesystem path to the directory for user-uploaded files.
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
# The public URL for handling files stored in MEDIA_ROOT.
MEDIA_URL = '/media/'


# ==============================================================================
# MISCELLANEOUS CORE SETTINGS
# ==============================================================================
# The default primary key field type for new models.
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"


# ==============================================================================
# THIRD-PARTY APP CONFIGURATION
# ==============================================================================
# Configuration for caching. This setup uses Memcached.
CACHES = {
    # The default cache backend for general use.
    "default": {
        "BACKEND": "django.core.cache.backends.memcached.PyMemcacheCache",
        "LOCATION": "127.0.0.1:11211",
        "OPTIONS": {
            "no_delay": True,
            "ignore_exc": True,
            "max_pool_size": 4,
            "use_pooling": True,
        },
    },
    # A separate cache configuration specifically for rate-limiting.
    'cache-for-ratelimiting': {
        "BACKEND": "django.core.cache.backends.memcached.PyMemcacheCache",
        "LOCATION": "127.0.0.1:11211",
        "OPTIONS": {
            "no_delay": True,
            "ignore_exc": True,
            "max_pool_size": 4,
            "use_pooling": True,
        },
    },
}

# Tells the `django-ratelimit` app to use the specific cache alias defined above.
RATELIMIT_USE_CACHE = 'cache-for-ratelimiting'

# Tells the `django-tailwind` app which app contains the theme and tailwind assets.
TAILWIND_APP_NAME = 'theme'

# A list of IP addresses that are considered "internal", used by tools
# like the Django Debug Toolbar to determine if they should be shown.
INTERNAL_IPS = [
    "127.0.0.1",
]

# A list of origins (scheme, host, port) that are allowed to make cross-site
# HTTP requests to this server.
CORS_ALLOWED_ORIGINS = [
    "http://127.0.0.1:8000",
]

# A list of origins that are trusted for CSRF purposes, necessary when your
# frontend and backend are on different subdomains or ports.
CSRF_TRUSTED_ORIGINS = [
    "http://127.0.0.1:3000",
]

# Configuration for `django-webpack-loader` to find the stats file generated
# by Webpack, which maps bundle names to their actual output files.
WEBPACK_LOADER = {
    "DEFAULT": {
        "BUNDLE_DIR_NAME": "frontend/",
        "STATS_FILE": os.path.join(BASE_DIR, "frontend/static/frontend/webpack-stats.json")
    }
}

# Sets the image size for `django-simple-captcha`.
CAPTCHA_IMAGE_SIZE = (100, 60)  # Width x Height in pixels


# ==============================================================================
# SECURITY SETTINGS
# ==============================================================================
# Defines allowed sources for stylesheets, enhancing Content Security Policy (CSP).
CSP_STYLE_SRC = ("'self'",)
# Defines allowed sources for scripts.
CSP_SCRIPT_SRC = ("'self'",)
# Instructs `django-csp` to automatically add a `nonce` attribute to script tags.
CSP_INCLUDE_NONCE_IN = ['script-src']

# Enables the browser's built-in XSS protection.
SECURE_BROWSER_XSS_FILTER = True
# Prevents the site from being rendered in an iframe to mitigate clickjacking attacks.
X_FRAME_OPTIONS = 'DENY'
# Prevents the browser from misinterpreting files' content types.
SECURE_CONTENT_TYPE_NOSNIFF = True

# Sets how long the browser should cache static files served by WhiteNoise (in seconds).
WHITENOISE_MAX_AGE = 31536000  # One year

# --- PRODUCTION-ONLY SETTINGS ---
# The settings in this block are only activated when DEBUG is False.
# This prevents them from causing issues in local development (like HTTPS redirects).
if not DEBUG:
    # Tells the browser to only send the CSRF cookie over HTTPS connections.
    CSRF_COOKIE_SECURE = True
    # Tells the browser to only send the session cookie over HTTPS connections.
    SESSION_COOKIE_SECURE = True
    # Redirects all non-HTTPS requests to HTTPS.
    SECURE_SSL_REDIRECT = True
    # Enables HTTP Strict Transport Security (HSTS), telling browsers to always use HTTPS.
    SECURE_HSTS_SECONDS = 31536000  # 1 year
    SECURE_HSTS_INCLUDE_SUBDOMAINS = True
    SECURE_HSTS_PRELOAD = True

    # An optimization for WhiteNoise in production.
    WHITENOISE_USE_FINDERS = False