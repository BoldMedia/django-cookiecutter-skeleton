from .common import *


##
## Debug Settings
################################################################################
DEBUG = env('DEBUG', default=False)
TEMPLATES[0]['OPTIONS']['debug'] = DEBUG


##
## Allowed Hosts Settings
################################################################################
ALLOWED_HOSTS = ['*']
