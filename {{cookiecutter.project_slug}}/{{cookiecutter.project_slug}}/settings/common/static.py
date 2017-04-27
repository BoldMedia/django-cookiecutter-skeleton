from os.path import join
from .paths import DJANGO_ROOT

# URL endpoint to access static and media files
STATIC_URL = '/static/'
MEDIA_URL = '/media/'

# File system paths where our static and media files
# are accessible in production
STATIC_ROOT = join(DJANGO_ROOT, 'public', 'assets')
MEDIA_ROOT = join(DJANGO_ROOT, 'public', 'media')

# Path and storage type for non-collected static files
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
STATICFILES_DIRS = [
    join(DJANGO_ROOT, 'static')
]
