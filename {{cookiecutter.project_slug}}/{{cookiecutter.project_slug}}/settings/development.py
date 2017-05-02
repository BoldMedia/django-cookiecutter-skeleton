from {{cookiecutter.project_slug}}.settings.base import *


##
## Debug Settings
#############################
DEBUG = True
TEMPLATE_DEBUG = DEBUG


##
## Allowed Hosts Settings
#############################
ALLOWED_HOSTS = []


##
## Debug Toolbar Settings
#############################
DEBUG_TOOLBAR_PATCH_SETTINGS = False
INSTALLED_APPS += ['debug_toolbar']
MIDDLEWARE_CLASSES += ['debug_toolbar.middleware.DebugToolbarMiddleware']
INTERNAL_IPS = ['127.0.0.1', '::1']
DEBUG_TOOLBAR_CONFIG = {'INTERCEPT_REDIRECTS': False}
