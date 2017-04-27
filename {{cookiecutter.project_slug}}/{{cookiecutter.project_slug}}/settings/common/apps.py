DJANGO_APPS = [
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.humanize'
]

THIRD_PARTY_APPS = [
    'whitenoise.runserver_nostatic',
    {% if cookiecutter.use_cas_auth.lower() == "y" %}'django_cas_ng'{% endif %}
]

LOCAL_APPS = []

INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS
