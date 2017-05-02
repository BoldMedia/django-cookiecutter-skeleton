"""Root URLs Setting File """

from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls import include, url
from django.conf import settings
{% if cookiecutter.use_cas_auth.lower() == 'y' -%}
from django_cas_ng.views import login, logout
{%- endif %}


urlpatterns = [
    {% if cookiecutter.use_cas_auth.lower() == 'y' -%}
    url(r'^login/$', login, name='login'),
    url(r'^logout/$', logout, name='logout')
    {%- endif %}
]

if settings.DEBUG:
    urlpatterns += staticfiles_urlpatterns()
    if 'debug_toolbar' in settings.INSTALLED_APPS:
        from debug_toolbar import urls as debug_toolbar_urls
        urlpatterns += [url(r'^__debug__/', include(debug_toolbar_urls))]
