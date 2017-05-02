from {{cookiecutter.project_slug}}.settings.base import *


##
## Debug Settings
################################################################################
DEBUG = env('DEBUG', default=True)
TEMPLATES[0]['OPTIONS']['debug'] = DEBUG


##
## Allowed Hosts Settings
################################################################################
ALLOWED_HOSTS = []


##
## Debug Toolbar Settings
################################################################################
DEBUG_TOOLBAR_PANELS = [
    'debug_toolbar.panels.versions.VersionsPanel',
    'debug_toolbar.panels.timer.TimerPanel',
    'debug_toolbar.panels.settings.SettingsPanel',
    'debug_toolbar.panels.headers.HeadersPanel',
    'debug_toolbar.panels.request.RequestPanel',
    'debug_toolbar.panels.sql.SQLPanel',
    'debug_toolbar.panels.staticfiles.StaticFilesPanel',
    'debug_toolbar.panels.templates.TemplatesPanel',
    'debug_toolbar.panels.cache.CachePanel',
    'debug_toolbar.panels.signals.SignalsPanel',
    'debug_toolbar.panels.logging.LoggingPanel',
    'debug_toolbar.panels.redirects.RedirectsPanel'
]
DEBUG_TOOLBAR_CONFIG = {'INTERCEPT_REDIRECTS': False}
DEBUG_TOOLBAR_PATCH_SETTINGS = False
INSTALLED_APPS += ['debug_toolbar']
MIDDLEWARE += ['debug_toolbar.middleware.DebugToolbarMiddleware']
INTERNAL_IPS = ['127.0.0.1', '::1']
