from os.path import abspath, basename, dirname, join, normpath
from sys import path
from random import choice


# ######### PATH CONFIGURATION
DJANGO_ROOT = dirname(dirname(abspath(__file__)))
SITE_ROOT = dirname(DJANGO_ROOT)
SITE_NAME = basename(DJANGO_ROOT)
SECRET_FILE = join(DJANGO_ROOT, '..', 'secret-key.txt')
path.append(DJANGO_ROOT)
# ######### END PATH CONFIGURATION


# ######### KEY CONFIGURATION
# Try to load the SECRET_KEY from our SECRET_FILE. If that fails, then generate
# a random SECRET_KEY and save it into our SECRET_FILE for future loading. If
# everything fails, then just raise an exception.
try:
    SECRET_KEY = open(SECRET_FILE).read().strip()
except Exception:
    try:
        with open(SECRET_FILE, 'w') as f:
            SECRET_KEY = ''.join([choice('abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*(-_=+)') for i in range(50)])
            f.write(SECRET_KEY)
    except IOError:
        raise Exception('Cannot open file `%s` for writing.' % SECRET_FILE)
# ######### END KEY CONFIGURATION


# ######### ALLOWED HOSTS CONFIGURATION
ALLOWED_HOSTS = []
# ######### END ALLOWED HOSTS CONFIGURATION


# ######### ADMIN CONFIGURATION
ADMINS = (
    ('Your Name', 'your@email.com')
)
MANAGERS = ADMINS
# ######### END ADMIN CONFIGURATION


# ######### TEMPLATE CONFIGURATION
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)
TEMPLATE_DIRS = (
    normpath(join(DJANGO_ROOT, 'templates')),
)
# ######### END TEMPLATE CONFIGURATION


# ######### MODULE CONFIGURATION
DJANGO_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.humanize'
)
THIRD_PARTY_APPS = ()
LOCAL_APPS = ()
INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS
# ######### END MODULE CONFIGURATION


# ######### MIDDLEWARE CONFIGURATION
DJANGO_MIDDLEWARE_CLASSES = (
    'django.middleware.cache.UpdateCacheMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware'
)
LOCAL_MIDDLEWARE_CLASSES = ()
MIDDLEWARE_CLASSES = DJANGO_MIDDLEWARE_CLASSES + LOCAL_MIDDLEWARE_CLASSES
# ######### END MIDDLEWARE CONFIGURATION


# ######## AUTHENTICATION BACKENDS
AUTHENTICATION_BACKENDS = (
    'apps.user_management.backends.IdModelBackend',
    'django.contrib.auth.backends.ModelBackend',
)
# ######## END AUTHENTICATION BACKENDS


# ######### REDIS CACHE AND SESSION HANDLING
CACHES = {
    'default': {
        'BACKEND': 'redis_cache.RedisCache',
        'LOCATION': '/var/run/redis/redis.sock'
    }
}

SESSION_ENGINE = 'django.contrib.sessions.backends.cache'
# ######### END REDIS CACHE AND SESSION HANDLING


# ######### URL CONFIGURATION
ROOT_URLCONF = '%s.urls' % SITE_NAME
# ######### END URL CONFIGURATION


# ######### WSGI CONFIGURATION
WSGI_APPLICATION = 'wsgi.application'
# ######### END WSGI CONFIGURATION


# ######### INTERNATIONALIZATION CONFIGURATION
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True
# ######### END INTERNATIONALIZATION CONFIGURATION


# ######### STATIC FILE CONFIGURATION
STATIC_URL = '/static/'
MEDIA_URL = '/media/'
STATIC_ROOT = join(DJANGO_ROOT, 'public', 'assets')
MEDIA_ROOT = join(DJANGO_ROOT, 'public', 'media')
STATICFILES_DIRS = [
    join(DJANGO_ROOT, 'assets')
]
# ######### END STATIC FILE CONFIGURATION


# ######### USER LOGIN URL
LOGIN_URL = '/user/login/'
# ######### END USER LOGIN URL
