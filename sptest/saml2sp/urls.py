from django.conf.urls.defaults import *
from views import sso_response, sso_test, sso_idp_select

urlpatterns = patterns('',
    # Example:
    # (r'^sptest/', include('sptest.foo.urls')),

    # Uncomment the admin/doc line below and add 'django.contrib.admindocs'
    # to INSTALLED_APPS to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # (r'^admin/', include(admin.site.urls)),

    (r'^test/$', sso_test),
    (r'^idpselect/$', sso_idp_select),
    (r'^acs/$', sso_response),
)
