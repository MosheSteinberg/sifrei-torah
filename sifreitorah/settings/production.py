from .base import *
from os import environ

DEBUG = False

SECRET_KEY = environ.get('DJANGO_SECRET_KEY')

try:
    from .local import *
except ImportError:
    pass
