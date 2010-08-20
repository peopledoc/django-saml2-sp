from django.conf.urls.defaults import *
from views import sso_login, sso_response

urlpatterns = patterns('',
    # Example:
    # (r'^sptest/', include('sptest.foo.urls')),

    # Uncomment the admin/doc line below and add 'django.contrib.admindocs'
    # to INSTALLED_APPS to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # (r'^admin/', include(admin.site.urls)),

    (r'^sso/login/', sso_login),
    (r'^sso/post/response/$', sso_response),
)
