"""Common settings for all environments """

import environ

from sys import path
from random import choice
from os.path import normpath, join, abspath, basename, dirname


##
## Path Settings
################################################################################
DJANGO_ROOT = dirname(dirname(abspath(__file__)))
SITE_ROOT = dirname(DJANGO_ROOT)
SITE_NAME = basename(DJANGO_ROOT)

path.append(DJANGO_ROOT)


##
## Environ Settings (Load 'Er Up!)
################################################################################
env = environ.Env()
environ.Env.read_env(join(SITE_ROOT, '.env'))


##
## Apps Settings
################################################################################
INSTALLED_APPS = [
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.humanize',
    'whitenoise.runserver_nostatic',
    'django.contrib.staticfiles',
    {% if cookiecutter.use_cas_auth.lower() == 'y' -%}
    'django_cas_ng'
    {%- endif %}
]


##
## Authentication Settings
################################################################################
LOGIN_URL = '/user/login/'
AUTHENTICATION_BACKENDS = [
    {% if cookiecutter.use_cas_auth.lower() == 'y' -%}
    'django_cas_ng.backends.CASBackend'
    {%- else -%}
    'django.contrib.auth.backends.ModelBackend'
    {%- endif %}
]
{%- if cookiecutter.use_cas_auth.lower() == 'y' %}
CAS_SERVER_URL = ''
CAS_IGNORE_REFERER = True
CAS_RETRY_LOGIN = True
CAS_VERSION = '3'
CAS_USERNAME_ATTRIBUTE = 'username'
CAS_FORCE_CHANGE_USERNAME_CASE = 'lower'
{%- endif %}


##
## Database Settings
#############################
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': env('DB_NAME'),
        'USER': env('DB_USER'),
        'PASSWORD': env('DB_PASS'),
        'HOST': env('DB_HOST', default='localhost'),
        'PORT': env('DB_PORT', default=5432)
    }
}


##
## Middleware Settings
#############################
DJANGO_MIDDLEWARE = [
    'django.middleware.cache.UpdateCacheMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware'
]
THIRD_PARTY_MIDDLEWARE = ['whitenoise.middleware.WhiteNoiseMiddleware']
LOCAL_MIDDLEWARE = []

MIDDLEWARE = DJANGO_MIDDLEWARE + THIRD_PARTY_MIDDLEWARE + LOCAL_MIDDLEWARE


##
## Templating Settings
################################################################################
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [normpath(join(DJANGO_ROOT, 'templates'))],
        'APP_DIRS': True,
        'OPTIONS': {}
    }
]


##
## Admins/Managers Settings
################################################################################
ADMINS = [['{{cookiecutter.author_name}}', '{{cookiecutter.author_email}}']]
MANAGERS = ADMINS + []


##
## WSGI Entry Point
################################################################################
WSGI_APPLICATION = '{{cookiecutter.project_slug}}.wsgi.application'


##
## Root URL File Settings
################################################################################
ROOT_URLCONF = '%s.urls' % SITE_NAME


##
## Internationalization/Localization Settings
################################################################################
LANGUAGE_CODE = 'en-us'
USE_I18N = True
USE_L10N = True
USE_TZ = True
TIME_ZONE = 'UTC'


##
## Secret Key Settings
################################################################################
SECRET_FILE = join(DJANGO_ROOT, '..', 'secret-key.txt')

# Try to load the SECRET_KEY from our SECRET_FILE. If that fails, then generate
# a random SECRET_KEY and save it into our SECRET_FILE for future loading. If
# everything fails, then just raise an exception.
try:
    with open(SECRET_FILE) as secret_file:
        SECRET_KEY = secret_file.read().strip()
except Exception:
    try:
        with open(SECRET_FILE, 'w') as f:
            char_choice = 'abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*(-_=+)'
            SECRET_KEY = ''.join([choice(char_choice) for i in range(50)])
            f.write(SECRET_KEY)
    except IOError:
        raise Exception('Cannot open file `%s` for writing.' % SECRET_FILE)


##
## HTTPS/Security Settings
################################################################################
SECURE_PROXY_SSL_HEADER = ['HTTP_X_FORWARDED_PROTO', 'https'] # Needed with Proxy


##
## HTTP Session Settings
################################################################################
SESSION_COOKIE_AGE = 60 * 60 * 24
SESSION_EXPIRE_AT_BROWSER_CLOSE = True


##
## Static/Media File Settings
################################################################################
STATIC_URL = '/static/'
MEDIA_URL = '/media/'

# File system paths where our static and media files are found. Static files
# are thrown there when running collectstatic
STATIC_ROOT = join(DJANGO_ROOT, 'public', 'assets')
MEDIA_ROOT = join(DJANGO_ROOT, 'public', 'media')

# Path and storage type for non-collected static files
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
STATICFILES_DIRS = [
    join(SITE_ROOT, 'static')
]
