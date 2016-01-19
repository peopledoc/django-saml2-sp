from django.conf.urls.defaults import url
from views import (
    descriptor,
    sso_idp_select,
    sso_response,
    sso_single_logout,
    sso_test,
)

urlpatterns = [
    # Example:
    # (r'^sptest/', include('sptest.foo.urls')),

    # Uncomment the admin/doc line below and add 'django.contrib.admindocs'
    # to INSTALLED_APPS to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # (r'^admin/', include(admin.site.urls)),

    url(r'^test/$', sso_test),
    url(r'^idpselect/$', sso_idp_select),
    url(r'^acs/$', sso_response),
    url(r'^singlelogout/$', sso_single_logout, name='sso_single_logout'),
    url(r'^metadata/', descriptor, name='spssodescriptor'),
]
