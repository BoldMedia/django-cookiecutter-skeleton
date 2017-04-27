from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django_cas_ng.views import login, logout
from django.conf.urls import include, url
from django.conf import settings


urlpatterns = [
    url(r'^login/$', login, name='login'),
    url(r'^logout/$', logout, name='logout')
]

if settings.DEBUG:
    urlpatterns += staticfiles_urlpatterns()
    if 'debug_toolbar' in settings.INSTALLED_APPS:
        from debug_toolbar import urls as debug_toolbar_urls
        urlpatterns += [url(r'^__debug__/', include(debug_toolbar_urls))]
