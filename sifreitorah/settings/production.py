from .base import *
from os import environ

DEBUG = False

SECRET_KEY = environ.get('DJANGO_SECRET_KEY')

ALLOWED_HOSTS = [environ.get('CURRENT_HOST')]

try:
    from .local import *
except ImportError:
    pass

import django_heroku

# Activate Django-Heroku.
django_heroku.settings(locals(), logging=False)