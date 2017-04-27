LOGIN_URL = '/user/login/'
AUTHENTICATION_BACKENDS = [
    {% if cookiecutter.use_cas_auth.lower() == 'y' %}
    'django_cas_ng.backends.CASBackend',
    {% else %}
    'django.contrib.auth.backends.ModelBackend',
    {% endif %}
]

{% if cookiecutter.use_cas_auth.lower == 'y' %}
CAS_SERVER_URL = ''
CAS_IGNORE_REFERER = True
CAS_RETRY_LOGIN = True
CAS_VERSION = '3'
CAS_USERNAME_ATTRIBUTE = 'username'
CAS_FORCE_CHANGE_USERNAME_CASE = 'lower'
{% endif %}
