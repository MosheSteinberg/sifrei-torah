from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'i$me6!qghmgiz(3ptwybjtn&*3d9a-#ac59k2u010hznowd256'


# SECURITY WARNING: define the correct hosts in production!
ALLOWED_HOSTS = ['*'] 


try:
    from .local import *
except ImportError:
    pass
