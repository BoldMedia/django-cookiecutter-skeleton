"""Common settings for all environments """

from os.path import normpath, join
from .paths import SITE_NAME, DJANGO_ROOT
from .security import *
from .database import *
from .apps import *
from .middleware import *
from .authentication import *
from .static import *


# Hostnames that are allowed to be used to access the site
ALLOWED_HOSTS = []

# Templating Loaders And Directories
TEMPLATE_LOADERS = [
    'django.template.loaders.filesystem.Loader',      # Search TEMPLATE_DIRS
    'django.template.loaders.app_directories.Loader'  # Search All Apps
]
TEMPLATE_DIRS = [normpath(join(DJANGO_ROOT, 'templates'))]

# Admins/Managers
ADMINS = [['{{cookiecutter.author_name}}', '{{cookiecutter.author_email}}']]
MANAGERS = ADMINS

# WSGI Entry Point
WSGI_APPLICATION = 'wsgi.application'

# Entrypoint For URLs
ROOT_URLCONF = '%s.urls' % SITE_NAME

# Internationalization
LANGUAGE_CODE = 'en-us'
USE_I18N = True
USE_L10N = True
USE_TZ = True
TIME_ZONE = 'UTC'


