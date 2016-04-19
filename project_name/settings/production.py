from .common import *


# ######### DEBUG CONFIGURATION
DEBUG = False
TEMPLATE_DEBUG = DEBUG
# ######### END DEBUG CONFIGURATION


# ######### DATABASE CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': '',
        'USER': '',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '',
    }
}
# ######### END DATABASE CONFIGURATION


# ######### ALLOWED HOSTS
ALLOWED_HOSTS = ['*']
# ######### END ALLOWED HOSTS
