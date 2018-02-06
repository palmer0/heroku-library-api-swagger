from .base import *
import dj_database_url


DATABASES['default'] = dj_database_url.config()

SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

ALLOWED_HOSTS = ['*']

DEBUG = False

# Configuration of CORS to receive the API response from Swagger UI
CORS_ORIGIN_ALLOW_ALL = True

WSGI_APPLICATION = 'config.wsgi_heroku.application'
