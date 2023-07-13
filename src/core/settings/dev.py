import os

from core.settings.base import *
from load_dotenv import load_dotenv

load_dotenv(".env.dev")

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get("PROJECT_SECRET_KEY")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ["*"]

# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": os.environ.get("POSTGRES_DB"),
        "USER": os.environ.get("POSTGRES_USER"),
        "PASSWORD": os.environ.get("POSTGRES_PASSWORD"),
        "HOST": os.environ.get("POSTGRES_HOST"),
        "PORT": os.environ.get("POSTGRES_PORT"),
    }
}

CELERY_TIMEZONE = "Europe/Kiev"
CELERY_TASK_TRACK_STARTED = True
CELERY_TASK_TIME_LIMIT = 30 * 60

REDIS_URL = os.environ.get("REDIS_URL")
REDIS_CACHE = os.environ.get("REDIS_CACHE")

CELERY_RESULT_BACKEND = REDIS_URL
CELERY_BROKER_URL = REDIS_URL

CACHES = {
    "default": {
        "BACKEND": "django.core.cache.backends.redis.RedisCache",
        "LOCATION": f"{REDIS_CACHE}",
    }
}
