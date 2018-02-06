from .base import *


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# CORS configuration to receive the API response from Swagger UI
CORS_ORIGIN_WHITELIST = (
    'localhost:8000'
)

WSGI_APPLICATION = 'config.wsgi.application'
